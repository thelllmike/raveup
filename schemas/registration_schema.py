# schemas/registration_schema.py
from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING, List
from enum import Enum
from datetime import datetime

# avoid circular import at runtime
if TYPE_CHECKING:
    from schemas.event_schema import EventOut

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

class RegistrationWithEvent(Registration):
    # string annotation prevents circular import at runtime
    event: "EventOut"

    class Config(Registration.Config):
        pass
