from datetime import datetime
from sqlmodel import SQLModel
from typing import Optional


class UserCreate(SQLModel):
    username: str
    email: str
    password: str  
    full_name: Optional[str] = None
 


class UserRead(SQLModel):
    # id: int
    username: str
    email: str
    # created_at: datetime

class UserLogin(SQLModel):
    email: str
    password: str
    
