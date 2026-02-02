import logging
from typing import Any, Dict, List
import requests
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from auth.Auth import verify_token
from models.monitoring_event_subscriptions import MonitoringEventSubscription

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
app = FastAPI()

class APISuccessResponse(BaseModel):
    message: str
    subscription: Dict[str, Any]

class DeleteResponse(BaseModel):
    message: str

class SubscriptionResponse(BaseModel):
    subscriptions: List[dict]

class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token  # Ajouter le token comme attribut de la classe


    def create_subscription(self, scsAsId: str, subscription: MonitoringEventSubscription):
        url = f"{self.base_url}/3gpp-monitoring-event/v1/{scsAsId}/subscriptions"
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

        try:
            response = requests.post(url, json=subscription.dict(), headers=headers)
            response.raise_for_status()
            return {
                "data": response.json(),  # Retourner les données JSON de la réponse
                "headers": response.headers,  # Retourner les en-têtes de la réponse
                "location": response.headers.get("Location")  # Retourner l'en-tête 'Location' s'il existe
            }
        except requests.exceptions.RequestException as e:
            # Ajouter des informations supplémentaires dans le message d'erreur
            return {"error": f"Request failed: {str(e)}, Status Code: {response.status_code}"}

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
async def create_subscription(scsAsId: str, subscription: MonitoringEventSubscription, token_data: dict = Depends(verify_token)):
    # Vérification de la présence de 'access_token'
    print("hada hoa",token_data)
    if 'access_token' not in token_data:
        raise HTTPException(status_code=401, detail="Token is missing 'access_token'")

    client = APIClient(base_url="http://event_monitoring_server:8005", token=token_data["access_token"])
    
    try:
        response = client.create_subscription(scsAsId, subscription)
        logger.debug("Response: %s", response)
        
        if "error" in response:
            raise HTTPException(status_code=500, detail=response["error"])

        data = response.get("data", {})
        headers = response.get("headers", {})
        location = response.get("location")

        logger.debug("Response Headers: %s", headers)
        
        json_response_content = {
            "message": "Subscription created successfully",
            "subscription": data
        }

        json_response_headers = {}
        if location:
            json_response_headers["Location"] = location

        return JSONResponse(content=json_response_content, headers=json_response_headers)
    
    except Exception as e:
        logger.error(f"Error creating JSONResponse: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions", response_model=SubscriptionResponse)
async def get_all_subscriptions(scsAsId: str):

    client = APIClient(base_url="http://event_monitoring_server:8005")
    response = client.get_all_subscriptions(scsAsId)

    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    subscriptions = response
    return subscriptions

@app.get("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=APISuccessResponse)
async def get_subscription_handler(scsAsId: str, subscriptionId: str):
    client = APIClient(base_url="http://event_monitoring_server:8005")
    response = client.get_subscription(scsAsId, subscriptionId)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    subscription_data = response
    return APISuccessResponse(message="Subscription retrieved successfully", subscription=subscription_data)

@app.put("/3gpp-monitoring-event/v1/{scsAsId}/subscriptions/{subscriptionId}", response_model=APISuccessResponse)
async def update_subscription_handler(scsAsId: str, subscriptionId: str, subscription: MonitoringEventSubscription):
    api_client = APIClient(base_url="http://event_monitoring_server:8005")
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
    api_client = APIClient(base_url="http://event_monitoring_server:8005")
    response = api_client.delete_subscription(scsAsId, subscriptionId)
    if "error" in response:
        raise HTTPException(status_code=500, detail=response["error"])

    return DeleteResponse(message="Subscription deleted successfully")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006)

