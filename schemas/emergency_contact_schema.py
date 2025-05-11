from pydantic import BaseModel
from typing import Optional

class EmergencyContactBase(BaseModel):
    contact_name: str
    relationship: Optional[str]
    contact_phone: Optional[str]

class EmergencyContactCreate(EmergencyContactBase):
    racer_id: int

class EmergencyContactUpdate(BaseModel):
    contact_name: Optional[str]
    relationship: Optional[str]
    contact_phone: Optional[str]

class EmergencyContact(EmergencyContactBase):
    id: int
    racer_id: int

    class Config:
        orm_mode = True
