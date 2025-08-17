from fastapi import FastAPI
from app.config.db import init_db


app = FastAPI()

def on_startup():
    init_db()
    print("Database initialized on startup.")

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/item/")
async def read_item():
    return {"item": "This is an item"}