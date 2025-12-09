from app.routers import users
from app.routers import items
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)
