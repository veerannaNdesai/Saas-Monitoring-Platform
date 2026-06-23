# pyrefly: ignore [missing-import]
import requests
from app.services.monitor_service import get_monitor_by_id
from app.models.user import User
import requests
from sqlalchemy.orm import Session
import time
from datetime import datetime


def check_health(
    id:int,
    current_user : User,
    db :Session    
    ):
    
    monitor = get_monitor_by_id(
        id,
        current_user,
        db
    )
    if not monitor:
        return None
    
    try: 

        start = time.time()

        response = requests.get(
            monitor.url,
            timeout=10
            )

        end = time.time()


        monitor.last_checked_at = datetime.utcnow()

        response_time = ( end - start ) * 1000

        if response.status_code == 200:
            monitor.status = "UP"
        else:
            monitor.status = "DOWN"
        
        monitor.response_time = response_time

    except requests.RequestException:
        monitor.status = "DOWN"
        monitor.response_time = None

    db.commit()
    db.refresh(monitor)

    return monitor





    

    