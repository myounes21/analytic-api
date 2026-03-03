from pydantic import BaseModel, Field
from typing import List, Optional



class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = Field(default="")



class EventUpdateSchema(BaseModel):
    description: str


class EventSchema(BaseModel):
    id: int
    page:Optional[str] = Field(default="home")
    description: Optional[str] = Field(default="")

class EventListSchema(BaseModel):
    results: List[EventSchema]
    count: int
