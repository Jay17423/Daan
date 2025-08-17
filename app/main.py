from fastapi import FastAPI
from app.config.db import create_db_and_tables
from contextlib import asynccontextmanager
from app.routes import auth   

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
