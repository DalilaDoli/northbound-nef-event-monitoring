# main.py

import uuid
from fastapi import FastAPI, Response
import requests
from models.monitoring_event_subscriptions import MonitoringEventSubscription
from models.monitoring_notification import MonitoringNotification, ConfigResult, MonitoringEventReport
import json

app = FastAPI()

last_subscription_id = 0

@app.post("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions")
async def create_subscription(scsAsId: str, subscription: MonitoringEventSubscription):
    global last_subscription_id
    last_subscription_id += 1

    subscription_id = last_subscription_id

    response_data = {
        "message from server": "Subscription created successfully",
        "subscriptionId": subscription_id,
        "subscription from server": subscription.model_dump(),
        "monitoringType": subscription.monitoringType

    }
    print("Le monitoring type est :", subscription.monitoringType)

    # Create notification
    notification = MonitoringNotification(
        subscription=f"subscription_id:{subscription_id}",
        configResults=[
            ConfigResult(externalIds=[""], msisdns=[""], resultReason="ROAMING_NOT_ALLOWED")
        ],
        monitoringEventReports=[
            MonitoringEventReport(monitoringType=subscription.monitoringType)
        ],
        addedExternalIds=["new_external_id"],
        addedMsisdns=["new_msisdn"],
        cancelExternalIds=[""],
        cancelMsisdns=[""],
        cancelInd=False
    )

    # send notification after create subscription
    try:
        notification_url = f"http://localhost:8001/3gpp-monitoring-event/v1/{subscription.notificationDestination}"
        notification_response = requests.post(notification_url, json=notification.dict())
        notification_response.raise_for_status()  
        print("Notification sent successfully")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(notification_response.text)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return Response(content=json.dumps(response_data), status_code=201, media_type="application/json")
