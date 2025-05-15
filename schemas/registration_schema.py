# schemas/registration_schema.py
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class RegistrationStatus(str, Enum):
    registered = "registered"
    payment_pending = "payment_pending"
    cancelled = "cancelled"

class RegistrationBase(BaseModel):
    racer_id: int
    event_id: int
    status: RegistrationStatus = RegistrationStatus.registered

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    status: Optional[RegistrationStatus]

class Registration(RegistrationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        use_enum_values = True
