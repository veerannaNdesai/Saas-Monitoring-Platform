from app.db.database import engine


try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
    
