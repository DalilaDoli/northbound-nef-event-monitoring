from typing import Any, Dict, List
import requests
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models.monitoring_event_subscriptions import MonitoringEventSubscription

app = FastAPI()

class APISuccessResponse(BaseModel):
    message: str
    subscription: Dict[str, Any]

class DeleteResponse(BaseModel):
    message: str

class SubscriptionResponse(BaseModel):
    subscriptions: List[dict]
class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_subscription(self, scsAsId: str, subscription: MonitoringEventSubscription):
        url = f"{self.base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions"
        try:
            response = requests.post(url, json=subscription.dict())
            response.raise_for_status()
            return {
                "data": response.json(),
                "headers": response.headers,
                "location": response.headers.get("Location")
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def get_all_subscriptions(self, scsAsId: str):
        url = f"{self.base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def get_subscription(self, scsAsId: str, subscriptionId: str):
        url = f"{self.base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def update_subscription(self, scsAsId: str, subscriptionId: str, updated_subscription: MonitoringEventSubscription):
            url = f"{self.base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}"
            try:
                response = requests.put(url, json=updated_subscription.dict())
                response.raise_for_status()
                return {
                    "data": response.json(),
                    "headers": response.headers,
                    "location": response.headers.get("Location")
                }
            except requests.exceptions.RequestException as e:
                return {"error": str(e)}
            
    def delete_subscription(self, scsAsId: str, subscriptionId: str):
        url = f"{self.base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return {"message": "Subscription deleted successfully"}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


@app.post("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions", response_model=APISuccessResponse)
async def create_subscription(scsAsId: str, subscription: MonitoringEventSubscription):
    client = APIClient(base_url="http://localhost:8000")
    response = client.create_subscription(scsAsId, subscription)
    print("Response:", response)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    data = response.get("data", {})
    headers = response.get("headers", {})
    location = response.get("location")

    print("Response Headers:", headers)

    # Création de la réponse JSON avec gestion des en-têtes
    json_response_content = {
        "message": "Subscription created successfully",
        "subscription": data
    }

    json_response_headers = {}
    if location:
        json_response_headers["Location"] = location

    try:
        return JSONResponse(content=json_response_content, headers=json_response_headers)
    except Exception as e:
        print(f"Error creating JSONResponse: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions", response_model=SubscriptionResponse)
async def get_all_subscriptions(scsAsId: str):
    client = APIClient(base_url="http://localhost:8000")
    response = client.get_all_subscriptions(scsAsId)
    
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    subscriptions = response  # Assuming response is a list of subscriptions or empty list
    return subscriptions

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=APISuccessResponse)
async def get_subscription_handler(scsAsId: str, subscriptionId: str):
    client = APIClient(base_url="http://localhost:8000")  # Replace with your actual server address
    response = client.get_subscription(scsAsId, subscriptionId)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    subscription_data = response
    return APISuccessResponse(message="Subscription retrieved successfully", subscription=subscription_data)

@app.put("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=APISuccessResponse)
async def update_subscription_handler(scsAsId: str, subscriptionId: str, subscription: MonitoringEventSubscription):
    api_client = APIClient(base_url="http://localhost:8000")
    response = api_client.update_subscription(scsAsId, subscriptionId, subscription)
    
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    data = response.get("data", {})
    headers = response.get("headers", {})
    location = response.get("location")

    json_response_content = {
        "message": "Subscription updated successfully",
        "subscription": data
    }

    json_response_headers = {}
    if location:
        json_response_headers["Location"] = location

    return JSONResponse(content=json_response_content, headers=json_response_headers)

@app.delete("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=DeleteResponse)
async def delete_subscription_handler(scsAsId: str, subscriptionId: str):
    api_client = APIClient(base_url="http://localhost:8000")
    response = api_client.delete_subscription(scsAsId, subscriptionId)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    return DeleteResponse(message="Subscription deleted successfully")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
