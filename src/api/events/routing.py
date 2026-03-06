from fastapi import Depends
from fastapi.routing import APIRouter
from sqlmodel import Session, select
from .models import (
    EventModel,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema
)
import os
from ..db.session import get_session

router = APIRouter()

@router.get("/", response_model=EventListSchema)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel).limit(5)
    results = session.exec(query).all()
    return {
        "results": results,
        "count":len(results)
    }

@router.post("/", response_model=EventModel)
def create_event(
        payload:EventCreateSchema,
        session: Session = Depends(get_session)
):
    print(payload.page)
    obj = EventModel.model_validate(payload)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.put("/{event_id}", response_model=EventModel)
def update_event(
        event_id:int,
        payload:EventUpdateSchema,
        session: Session = Depends(get_session)
):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()

    data = payload.model_dump()
    for k, v in data.items():
        setattr(obj, k, v)

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

@router.get("/{event_id}", response_model=EventModel)
def get_event(
        event_id: int,
        session: Session = Depends(get_session)
):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first()
    return result





@router.get("/test")
def read_events():
    print(os.environ.get("DATABASE_URL"))
    print("done!")
    return {
        "ok"
    }


