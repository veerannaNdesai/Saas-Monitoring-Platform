from app.models.monitor import Monitor
from app.models.user import User
from app.models.monitor_log import MonitorLog
from app.db.database import Base,engine

Base.metadata.create_all(bind=engine)
print(Base.metadata.tables.keys())
print("Tables created successfully")