from fastapi import FastAPI
from src.api.events import router as event_router

app = FastAPI()
app.include_router(event_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"status": "ok"}

