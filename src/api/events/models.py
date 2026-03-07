from sqlmodel import SQLModel, Field, Column
import sqlmodel
from typing import List, Optional
from datetime import datetime, timezone
from timescaledb import TimescaleModel
from timescaledb.utils import get_utc_now


class EventModel(TimescaleModel, table=True):
    page:str = Field(index=True)
    description: Optional[str] = Field(default="")


class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")

class EventUpdateSchema(SQLModel):
    description: str

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int
