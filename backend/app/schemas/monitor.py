from pydantic import HttpUrl
from pydantic import BaseModel
from datetime import datetime


class CreateMonitorRequest(BaseModel):
    name : str
    url : HttpUrl


class MonitorResponse(BaseModel):
        id: int
        name: str
        url: str
        check_interval: int
        status: str
        created_at: datetime
        last_checked_at: datetime | None