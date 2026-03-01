from fastapi.routing import APIRouter
from .schemas import EventSchema
router = APIRouter()

@router.get("/")
def read_events():
    return {
        "id": [1,2,3]
    }

@router.get("/{event_id}")
def get_evnt(event_id:int) ->EventSchema :
    return EventSchema(id=event_id)