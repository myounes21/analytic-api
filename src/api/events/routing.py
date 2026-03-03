from fastapi.routing import APIRouter
from .schemas import (
    EventSchema,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema
)
router = APIRouter()

@router.get("/", response_model=EventListSchema)
def read_events():
    return {
        "results": [
            {"id": 1}, {"id": 2}
        ],
        "count": 3
    }


@router.post("/", response_model=EventSchema)
def create_event(payload:EventCreateSchema):
    print(payload.page)
    data = payload.model_dump()
    return {
        "id": 123,
        **data
    }


@router.put("/{event_id}", response_model=EventSchema)
def update_event(event_id:int, payload:EventUpdateSchema):
    print(payload)
    data = payload.model_dump()
    return {
        "id": event_id,
        **data
    }



