from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from os import name
from sqlalchemy.orm import Session
from app.schemas.monitor import CreateMonitorRequest,MonitorEditRequest
from app.models.monitor import Monitor





def create_monitor(
    monitor_data : CreateMonitorRequest,
    db : Session ,
    current_user : User
):

    existing_monitor = db.query(
        Monitor
    ).filter(
            Monitor.url == str(monitor_data.url),
            Monitor.user_id == current_user.id
    ).first()

    if not existing_monitor:

        monitor = Monitor(
            name=monitor_data.name,
            url=str(monitor_data.url),
            check_interval=5,
            status="PENDING",
            user_id = current_user.id
    )
        db.add(monitor)
        db.commit()
        db.refresh(monitor)

        return monitor
    else:
        raise ValueError('Monitor already exists.')

    
def get_monitors(
    current_user:User,
    db : Session
    ):
    return (
        db.query(Monitor)
        .filter(current_user.id == Monitor.user_id)
        .all()
    )

def get_monitor_by_id(
    current_user:User,
    db : Session,
    monitor_id : int
):
    return (
        db.query(Monitor)
        .filter(current_user.id == Monitor.user_id,Monitor.id == monitor_id)
        .first()
    )

def delete_monitor_by_id(
    current_user:User,
    db : Session,
    monitor_id : int
):
    
    monitor = db.query(
            Monitor
        ).filter(
            Monitor.id == monitor_id ,
            Monitor.user_id == current_user.id
            ).first()

    if not monitor:
        return False

    db.delete(monitor)
    db.commit()

    return True

def update_monitor(
    current_user:User,
    db : Session,
    monitor_id : int,
    monitor_data : MonitorEditRequest
):
    monitor = db.query(
            Monitor
        ).filter(
            Monitor.id == monitor_id ,
            Monitor.user_id == current_user.id
            ).first()

    if not monitor:
        return None
    
    if monitor_data.name is not None:
        monitor.name = monitor_data.name

    if monitor_data.url is not None:
        monitor.url = str(monitor_data.url)

    db.commit()
    db.refresh(monitor)

    return monitor

    

    