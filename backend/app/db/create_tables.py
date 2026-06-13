from app.models.monitor import Monitor
from app.models.user import User
from app.db.database import Base,engine

Base.metadata.create_all(bind=engine)
print(Base.metadata.tables.keys())
print("Tables created successfully")