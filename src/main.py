from fastapi import FastAPI
from src.api.events import router as event_router
from contextlib import asynccontextmanager
from api.db.session import init_db

@asynccontextmanager
async def lifespane(app:FastAPI):
    init_db()
    yield
app = FastAPI(lifespan=lifespane)
app.include_router(event_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"status": "ok"}

