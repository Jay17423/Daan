from app.config.settings import settings


from sqlmodel import SQLModel,Field,create_engine, Session
from typing import Optional
from app.models.user import User



engine = create_engine(settings.DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



