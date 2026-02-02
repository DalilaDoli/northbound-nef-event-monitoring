import os
import logging
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError
from pymongo import MongoClient
from typing import List, Optional, Dict, Any
from pymongo.errors import AutoReconnect
from auth.Auth import verify_token
from auth.Auth import app as auth_app
from models.monitoring_event_subscriptions import MonitoringEventSubscription
from models.monitoring_notification import MonitoringNotification
import requests
from datetime import datetime, timedelta


# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# MongoDB connection
mongo_host = os.getenv('MONGO_HOST', 'mongo_fing')
mongo_port = int(os.getenv('MONGO_PORT', 27017))
client = MongoClient(mongo_host, mongo_port)
db = client.event_monitoring
collection = db.eventMonitoringSubscriptions
collection_notif = db.monitoring_notifications

# MongoDB connection to camara_mongo
camara_mongo_client = MongoClient("mongodb://camara_mongo:27017")
camara_db = camara_mongo_client["camara_api_db"]
camara_collection_notif = camara_db["notifications"]

app = FastAPI()

app.mount("/auth", auth_app)

class SubscriptionResponse(BaseModel):
    subscriptions: List[dict]

def get_next_sequence(name):
    try:
        counters = db.counters
        counter = counters.find_one_and_update(
            {"_id": name},
            {"$inc": {"seq": 1}},
            upsert=True,
            return_document=True
        )
        return counter['seq']
    except AutoReconnect:
        pass

def insert_subscription(subscription_dict):
    subscription_dict['_id'] = get_next_sequence('subscription_id')
    result = collection.insert_one(subscription_dict)
    return subscription_dict['_id']

def forward_to_nef_core(scsAsId, subscription_dict):
    nef_core_url = "http://nef_core:8002/nef-core/event-monitoring/subscribe"
    try:
        subscription_request_data = {
            "scsAsId": scsAsId,
            "subscription": subscription_dict
        }

        response = requests.post(nef_core_url, json=subscription_request_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error forwarding to NEF Core: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error forwarding to NEF Core: {str(e)}")

@app.post("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions")
async def create_subscription(scsAsId: str, subscription: MonitoringEventSubscription,token_data: dict = Depends(verify_token)):
    try:
        subscription_dict = subscription.dict()
        subscription_dict['scsAsId'] = scsAsId
        inserted_id = insert_subscription(subscription_dict)

        # forwarded_response = forward_to_nef_core(scsAsId, subscription_dict)

        return {
            "message": "Subscription created successfully",
            "subscription_id": inserted_id,
            "subscription": subscription,
            # "nef_core_response": forwarded_response
        }
    except Exception as e:
        logger.error(f"Error creating subscription: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error creating subscription: {str(e)}")

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions", response_model=SubscriptionResponse)
async def get_subscriptions(scsAsId: str):
    try:
        matching_subscriptions = list(collection.find({"scsAsId": scsAsId}))

        if not matching_subscriptions:
            raise HTTPException(status_code=404, detail="No subscriptions found for the provided SCS/AS ID")

        subscriptions = []
        for sub in matching_subscriptions:
            sub_copy = sub.copy()
            if '_id' in sub_copy:
                sub_copy['subscription_id'] = str(sub_copy.pop('_id'))
            subscriptions.append(sub_copy)

        return {"subscriptions": subscriptions}
    except Exception as e:
        logger.error(f"Error getting subscriptions: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get subscriptions: {str(e)}")

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscription_id}")
async def get_subscription(scsAsId: str, subscription_id: int):
    try:
        subscription = collection.find_one({"_id": subscription_id, "scsAsId": scsAsId})

        if subscription is None:
            raise HTTPException(status_code=404, detail="Subscription not found")

        return {"subscription": subscription}
    except Exception as e:
        logger.error(f"Error fetching subscription: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch subscription: {str(e)}")

@app.put("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=MonitoringEventSubscription)
async def update_subscription(scsAsId: str, subscriptionId: int, subscription: MonitoringEventSubscription):
    try:
        update_result = collection.update_one(
            {"_id": subscriptionId, "scsAsId": scsAsId},
            {"$set": subscription.dict(exclude_unset=True)}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Subscription not found")

        return subscription
    except Exception as e:
        logger.error(f"Error updating subscription: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to update subscription: {str(e)}")

@app.delete("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}")
async def delete_subscription(scsAsId: str, subscriptionId: int):
    try:
        query = {"_id": subscriptionId, "scsAsId": scsAsId}
        result = collection.delete_one(query)

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Subscription not found")

        return {"message from server": "Subscription deleted successfully"}
    except Exception as e:
        logger.error(f"Error deleting subscription: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to delete subscription: {str(e)}")

@app.post("/3gpp-monitoring-event/v1/notifications")
async def receive_monitoring_notification(request: Request):
    try:
        notification_data = await request.json()
        logger.debug(f"Received notification: {notification_data}")

        try:
            notification = MonitoringNotification(**notification_data)
        except ValidationError as e:
            logger.error(f"Validation error: {e.json()}")
            raise HTTPException(status_code=422, detail=e.errors())

        notification_dict = notification.dict(exclude_unset=True)

        # Insert into external MongoDB (camara_mongo)
#        inserted_result_camara = camara_collection_notif.insert_one(notification_dict)
#        logger.debug(f"Notification stored in camara_mongo successfully: {inserted_result_camara.inserted_id}")

        return {"message": "Notification received and stored successfully", "Received notification": notification}

    except Exception as e:
        logger.error(f"Error storing notification: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to store notification: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
