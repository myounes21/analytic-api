from sqlmodel import SQLModel, Field, Column
import sqlmodel
from typing import List, Optional
from datetime import datetime, timezone


def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    page:Optional[str] = Field(default="home")
    description: Optional[str] = Field(default="")
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_column=Column(sqlmodel.DateTime(timezone=True), nullable=False)
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_column=Column(sqlmodel.DateTime(timezone=True), nullable=False)
    )

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default="")

class EventUpdateSchema(SQLModel):
    description: str

class EventListSchema(SQLModel):
    results: List[EventModel]
    count: int
