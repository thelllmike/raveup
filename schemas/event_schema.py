from pydantic import BaseModel
from datetime import date
from typing import Optional, List
from .registration_schema import Registration

class EventBase(BaseModel):
    name: str
    event_date: date
    location: str
    category: str

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    name: Optional[str]
    event_date: Optional[date]
    location: Optional[str]
    category: Optional[str]

class EventOut(EventBase):
    id: int
    registrations: List[Registration] = []

    class Config:
        orm_mode = True

EventOut.model_rebuild()