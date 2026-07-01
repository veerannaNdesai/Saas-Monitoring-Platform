from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from app.schemas.monitor import MonitorLogResponse
from app.core.dependencies import get_current_user,get_db
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.monitor_log import MonitorLog

from app.services.monitor_log_service import get_monitorLogs

router = APIRouter(
    prefix = '/monitors/history',
    tags=['MonitorLogs']
)

@router.get(
    '/{id}',
    response_model = list[MonitorLogResponse]
)
def get_monitorlogs_endpoint(
    id : int,
    db : Session = Depends(get_db),
    user : User = Depends(get_current_user)
    
):
    monitor_logs = get_monitorLogs(
        id,
        db,
        user
    )
    
    if not monitor_logs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MonitorLogs not found"
        )
    return monitor_logs
    

