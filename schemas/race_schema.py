from pydantic import BaseModel
from datetime import date
from typing import Optional

class RaceBase(BaseModel):
    race_name: str
    location: str
    date: date
    category: str
    max_participants: int

class RaceCreate(RaceBase):
    pass

class RaceUpdate(BaseModel):
    race_name: Optional[str] = None
    location: Optional[str] = None
    date: Optional[date] = None
    category: Optional[str] = None
    max_participants: Optional[int] = None

class RaceOut(RaceBase):
    id: int

    class Config:
        orm_mode = True
