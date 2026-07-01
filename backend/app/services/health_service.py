# pyrefly: ignore [missing-import]
import requests
from app.services.monitor_service import get_monitor_by_id
from app.models.user import User
from app.models.monitor import Monitor
import requests
from sqlalchemy.orm import Session
import time
from datetime import datetime
from app.models.monitor_log import MonitorLog

def check_monitor(
    monitor : Monitor,
    db : Session
):
    
    try: 

        start = time.time()

        response = requests.get(
            monitor.url,
            timeout=10
            )

        end = time.time()


        monitor.last_checked_at = datetime.utcnow()

        response_time = int(( end - start ) * 1000)

        if response.status_code == 200:
            monitor.status = "UP"
        else:
            monitor.status = "DOWN"
        
        monitor.response_time = response_time

    except requests.RequestException:
        monitor.status = "DOWN"
        monitor.response_time = None
        monitor.last_checked_at = datetime.utcnow()
        
    monitor_log = MonitorLog(
            monitor_id = monitor.id,
            status = monitor.status,
            response_time = monitor.response_time,
            checked_at = datetime.utcnow()
        )
        
    db.add(monitor_log)
    db.commit()
    db.refresh(monitor)
    db.refresh(monitor_log)
        


    return {
        "monitor" : monitor,
        "monitor_log" : monitor_log
    }
    
    
    
    
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
    
    return check_monitor(
        monitor=monitor,
        db=db
    )
    






    

    