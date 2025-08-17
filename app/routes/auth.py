from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from app.config.db import engine
from app.models.user import User
from app.schema.user import UserCreate, UserRead, UserLogin
from app.utils.security import hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", response_model=UserRead) # userRead ka mtlab hai ki jab user signup karega, to response me UserRead schema ke according data milega
def signup(user: UserCreate):   #UserCreate ka mtlab hai client se jo data aayega, wo UserCreate schema ke according hoga
    with Session(engine) as session:
       
        existing_email = session.exec(select(User).where(User.email == user.email)).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        
        existing_username = session.exec(select(User).where(User.username == user.username)).first()
        if existing_username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        db_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password) 
        )

        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

@router.post("/login")
def login(user: UserLogin):
    with Session(engine) as session:
        db_user = session.exec(select(User).where(User.email == user.email)).first()
        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        return {
            "message": "Login successful",
            "user": UserRead.from_orm(db_user) 
        }
    