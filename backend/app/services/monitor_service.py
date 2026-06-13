from app.models.user import User
from os import name
from sqlalchemy.orm import Session
from app.schemas.monitor import CreateMonitorRequest
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
            Monitor.user_id == current_user
    ).first()

    if not existing_monitor:

        monitor = Monitor(
            name=monitor_data.name,
            url=str(monitor_data.url),
            check_interval=5,
            status="PENDING",
            user_id = current_user
    )
        db.add(monitor)
        db.commit()
        db.refresh(monitor)

        return monitor
    else:
        raise ValueError('Monitor already exists.')

    


    