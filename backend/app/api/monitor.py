

# pyrefly: ignore [missing-import]
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.core.dependencies import get_current_user

from app.models.user import User

from app.schemas.monitor import (
    CreateMonitorRequest,
    MonitorResponse
)

from app.services.monitor_service import (
    create_monitor
)


router = APIRouter(
    prefix = '/monitors',
    tags = ['Monitors']
)

@router.post(
    "",
    response_model=MonitorResponse
)
def create_monitor_endpoint(
    monitor_data: CreateMonitorRequest,
    current_user: User = Depends(
        get_current_user
    ),
    db: Session = Depends(
        get_db
    )
):
    
    try:
        return create_monitor(
            monitor_data,
            db,
            current_user
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )