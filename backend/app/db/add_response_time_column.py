from sqlalchemy import text
from app.db.database import engine

def add_column():
    try:
        with engine.connect() as connection:
            connection.execute(text("ALTER TABLE monitors ADD COLUMN IF NOT EXISTS response_time INTEGER;"))
            connection.commit()
            print("Successfully added column 'response_time' to 'monitors' table.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    add_column()
