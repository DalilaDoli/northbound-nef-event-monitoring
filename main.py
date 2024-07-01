from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from enum import Enum
from pymongo.errors import AutoReconnect
from models.monitoring_event_subscriptions import MonitoringEventSubscription
from models.monitoring_notification import MonitoringNotification



client = MongoClient('localhost', 27017)
db = client.test  
collection = db.monitoring_event_subscriptions  
collection_notif = db.monitoring_notifications

app = FastAPI()

next_subscription_id = 1

class SubscriptionResponse(BaseModel):
    subscriptions: List[dict]

class OneSubscriptionResponse(BaseModel):
    subscriptionId: str
    subscription: dict
    monitoringType: str

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

@app.post("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions")
async def create_subscription(scsAsId: str, subscription: MonitoringEventSubscription):
    try:
        subscription_dict = subscription.dict()
        subscription_dict['scsAsId'] = scsAsId 
        inserted_id = insert_subscription(subscription_dict)

        return {
            "message": "Souscription créée avec succès",
            "subscription_id": str(inserted_id),  
            "subscription": subscription  
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la création de la souscription: {str(e)}")

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions", response_model=SubscriptionResponse)
async def get_subscriptions(scsAsId: str):
    matching_subscriptions = list(collection.find({"scsAsId": scsAsId}))

    if not matching_subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for the provided SCS/AS ID")
    
    # Construire la liste des souscriptions sans inclure le champ subscription_id dans la réponse
    subscriptions = []
    for sub in matching_subscriptions:
        sub_copy = sub.copy()
        if '_id' in sub_copy:
            sub_copy['subscription_id'] = str(sub_copy.pop('_id'))
        subscriptions.append(sub_copy)

    return {"subscriptions": subscriptions}

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscription_id}")
async def get_subscription(scsAsId: str, subscription_id: int):
    try:
        subscription = collection.find_one({"_id": subscription_id, "scsAsId": scsAsId})

        if subscription is None:
            raise HTTPException(status_code=404, detail="Subscription not found")

        response = {
            "subscription": subscription,
           
        }

        return response

    except HTTPException as e:
        raise e
    except Exception as e:
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

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update subscription: {str(e)}")

@app.delete("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}")
async def delete_subscription(scsAsId: str, subscriptionId: int):
    try:
        query = {"_id": subscriptionId, "scsAsId": scsAsId}
        result = collection.delete_one(query)

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Subscription not found")

        return {"message from server": "Subscription deleted successfully"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete subscription: {str(e)}")
    
@app.post("/3gpp-monitoring-event/v1/{notificationDestination}")
async def receive_monitoring_notification(notificationDestination: str, notification: MonitoringNotification):
    try:
        notification_dict = notification.dict()
        notification_dict['notificationDestination'] = notificationDestination  
        inserted_result = collection_notif.insert_one(notification_dict)

        print("Received notification:", notification)

        return {"message": "Notification received and stored successfully", "Received notification:": notification}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to store notification: {str(e)}")


    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
