from typing import Any, Dict, List
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models.monitoring_event_subscriptions import MonitoringEventSubscription
import json

from models.monitoring_notification import MonitoringNotification

app = FastAPI()

class SubscriptionResponse(BaseModel):
    message: str
    subscriptions: List[Dict[str, Any]]
    
last_subscription_id = 0

subscriptions_db: Dict[int, MonitoringEventSubscription] = {}
scsAsId_subscriptions_mapping: Dict[int, str] = {}


@app.post("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions")
async def create_subscription(scsAsId: str, subscription: MonitoringEventSubscription):
    global last_subscription_id

    last_subscription_id += 1

    subscription_id = last_subscription_id
    subscriptions_db[subscription_id] = subscription

    scsAsId_subscriptions_mapping[last_subscription_id] = scsAsId  # Stocker scsAsId en relation avec subscription_id

    response_data = {
        "message from server": "Subscription created successfully",
        "subscriptionId": subscription_id,
        "subscription from server": subscription.model_dump(),
        "monitoringType": subscription.monitoringType,
                "scsAsId from server": scsAsId

    }

    print("Le monitoring type est :", subscription.monitoringType)
    print("La subscription type est :", subscription)

    return JSONResponse(content=response_data, status_code=201)

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions", response_model=SubscriptionResponse)
async def get_subscriptions(scsAsId: str):
    matching_subscriptions = []
    for subscription_id, subscription in subscriptions_db.items():
        if scsAsId_subscriptions_mapping.get(subscription_id) == scsAsId:
            subscription_with_id = subscription.model_dump()
            subscription_with_id["subscription_id"] = subscription_id
            matching_subscriptions.append(subscription_with_id)
    
    if not matching_subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for the provided SCS/AS ID")
    
    return SubscriptionResponse(message="Subscriptions found from server", subscriptions=matching_subscriptions)

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscription_id}")
async def get_subscription(scsAsId: str, subscription_id: int):
    

    if subscription_id not in subscriptions_db:
        raise HTTPException(status_code=404, detail="Subscription not found")

    subscription = subscriptions_db[subscription_id]

    return {
        "message from server": "Subscription found",
        "subscriptionId": subscription_id,
        "subscription from server": subscription.model_dump(),
        "monitoringType": subscription.monitoringType
    }

@app.put("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=MonitoringEventSubscription)
async def update_subscription(scsAsId: str, subscriptionId: int, subscription: MonitoringEventSubscription):
    if subscriptionId not in subscriptions_db:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    # Mettre à jour la subscription dans la base de données
    subscriptions_db[subscriptionId] = subscription

    return subscription

@app.delete("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}")
async def delete_subscription(scsAsId: str, subscriptionId: int):
    if subscriptionId not in subscriptions_db:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    # Supprimer la subscription de la base de données
    del subscriptions_db[subscriptionId]
    
    return {
        "message from server": "Subscription deleted successfully"
    }

@app.post("/3gpp-monitoring-event/v1/{notificationDestination}")
async def receive_monitoring_notification(notificationDestination: str, notification: MonitoringNotification):
    print("Received notification:", notification)

    return {"message": "Notification received successfully"}, notification