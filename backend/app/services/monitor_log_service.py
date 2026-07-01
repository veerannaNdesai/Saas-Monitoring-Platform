from app.schemas.monitor import MonitorLogResponse
from app.core.dependencies import get_current_user,get_db
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.monitor_log import MonitorLog
from app.models.monitor import Monitor

from app.services.monitor_service import get_monitor_by_id

def get_monitorLogs(
    monitor_id : int,
    db : Session,
    current_user : User
):
    monitor = get_monitor_by_id(
        monitor_id=monitor_id,
        current_user=current_user,
        db=db
    )
    
    if monitor:
        
        monitor_logs = db.query(MonitorLog)\
            .filter(MonitorLog.monitor_id == monitor.id)\
                .order_by(MonitorLog.checked_at.desc())\
                    .all()
                    
        return monitor_logs
    
    