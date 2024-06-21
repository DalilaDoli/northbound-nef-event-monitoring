# client.py

import requests
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from models.monitoring_notification import MonitoringNotification

app = FastAPI()

@app.post("/3gpp-monitoring-event/v1/{notificationDestination}")
async def receive_notification(notificationDestination: str, notification: MonitoringNotification):
    print(f"Received notification at {notificationDestination}: {notification}")
    return {"message": "Notification received successfully"}

def send_subscription(scsAsId, subscription_data):
    base_url = "http://localhost:8000"  

    try:
        url = f"{base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions"
        response = requests.post(url, json=subscription_data)
        response.raise_for_status()  # exception for HTTP requests
        print("Response from server:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#test client
if __name__ == "__main__":
    import threading
    import time

    def run_client_api():
        uvicorn.run(app, host="0.0.0.0", port=8001)

    # start client
    client_thread = threading.Thread(target=run_client_api)
    client_thread.start()

    # wait for client server to be ready
    time.sleep(2)

    scsAsId = "12345"  
    subscription_data = {
        "notificationDestination": "test_destination",
        "monitoringType": "LOCATION_REPORTING"
    }
    send_subscription(scsAsId, subscription_data)
