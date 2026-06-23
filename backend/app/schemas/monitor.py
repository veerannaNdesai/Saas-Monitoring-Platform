from pydantic import HttpUrl
from pydantic import BaseModel
from datetime import datetime




class MonitorInfo(BaseModel):
    name: str
    url: HttpUrl

class CreateMonitorRequest(MonitorInfo):
    pass

class MonitorResponse(MonitorInfo):
    check_interval: int
    status: str
    created_at: datetime
    response_time : int | None
    last_checked_at: datetime | None    

class MonitorEditRequest(BaseModel):
    name : str | None = None
    url : HttpUrl | None = None
