# pyrefly: ignore [missing-import]

from apscheduler.schedulers.background import BackgroundScheduler
from app.db.database import SessionLocal
from app.models.monitor import Monitor
from app.services.health_service import check_monitor

scheduler = BackgroundScheduler()

def monitor_job():
    
    print('scheduler is running...')
    db = SessionLocal()
    
    try:
        

        monitors = db.query(Monitor).all()
    
        for monitor in monitors:
            try:
                check_monitor(
            monitor,
            db
            )
            except Exception as e:
                print(f'{type(e)} : {e}')
                
    
    
    except Exception as e:
        print(f'{type(e)} : {e}')
        
    finally:
        db.close()
        

scheduler.add_job(
    monitor_job,
    trigger='interval',
    minutes = 5
)

def start_scheduler():
    scheduler.start()
    
def stop_scheduler():
    scheduler.shutdown()
    

        









