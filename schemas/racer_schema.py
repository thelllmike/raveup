from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, List
from .emergency_contact_schema import EmergencyContact
from .document_schema import RacerDocument
from .registration_schema import Registration
from .leaderboard_schema import Leaderboard

class RacerBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    nationality: Optional[str]
    email: EmailStr
    phone: Optional[str]

class RacerCreate(RacerBase):
    password: str
    racer_type: Optional[str]
    racing_team: Optional[str]

class RacerUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[date]
    nationality: Optional[str]
    phone: Optional[str]
    password: Optional[str]
    racer_type: Optional[str]
    racing_team: Optional[str]

class RacerOut(RacerBase):
    id: int
    racer_type: Optional[str]
    racing_team: Optional[str]
    created_at: datetime
    updated_at: datetime
    emergency_contacts: List[EmergencyContact] = []
    documents: List[RacerDocument] = []
    registrations: List[Registration] = []
    leaderboard_entries: List[Leaderboard] = []

    class Config:
        orm_mode = True
