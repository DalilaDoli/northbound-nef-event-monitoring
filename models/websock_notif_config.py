


from typing import ClassVar, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr


class WebsockNotifConfig(BaseModel):
   
    websocket_uri: Optional[StrictStr] = Field(default=None, description="string formatted according to IETF RFC 3986 identifying a referenced resource.", alias="websocketUri")
    request_websocket_uri: Optional[StrictBool] = Field(default=None, description="Set by the SCS/AS to indicate that the Websocket delivery is requested.", alias="requestWebsocketUri")
    __properties: ClassVar[List[str]] = ["websocketUri", "requestWebsocketUri"]