

# pyrefly: ignore [missing-import]
from app.services.monitor_service import update_monitor
from app.services.monitor_service import get_monitor_by_id,delete_monitor_by_id
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
from app.schemas.auth import UserResponse

from app.schemas.monitor import (
    CreateMonitorRequest,
    MonitorResponse,
    MonitorEditRequest
)

from app.services.monitor_service import (
    create_monitor,get_monitors
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

@router.get(
    '',
    response_model = list[MonitorResponse]
    )
def get_monitors_endpoint(
    current_user:User = Depends(get_current_user),
    db : Session = Depends(get_db)):
    return (
        get_monitors(current_user,db)
    )

@router.get(
    '/{id}',
    response_model = MonitorResponse
    )
def get_monitor_by_id_endpoint(
    id : int,
    current_user:User = Depends(get_current_user),
    db : Session = Depends(get_db)):
    monitor = get_monitor_by_id(current_user, db, id)
    if not monitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Monitor not found"
        )
    return monitor

@router.delete(
    '/{monitor_id}'
)
def delete_monitor(
    monitor_id : int,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    deleted = delete_monitor_by_id(
        current_user,db,monitor_id
    )
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Monitor not found."
        )

    return {
        "message": "Monitor deleted successfully."}

@router.patch(
    '/{id}'
)
def update_monitor_endpoint(
    monitor_data : MonitorEditRequest,
    id : int,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user),
):
    monitor  = update_monitor(
        current_user,
        db,
        monitor_id=id,
        monitor_data=monitor_data
    )

    if not monitor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Monitor not found"
        )
    return monitor

@router.get("/test",response_model=UserResponse)
def get_monitors_related_to_users(
    user: User = Depends(get_current_user)
):
    return user
