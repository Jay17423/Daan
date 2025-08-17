from sqlmodel import SQLModel, create_engine
from app.config.settings import settings


engine = create_engine(settings.DATABASE_URL, echo=True)

def init_db():
    try:
        with engine.connect() as conn:
            print("Database connection successful!")
    except Exception as e:
        print("Database connection failed:", e)
