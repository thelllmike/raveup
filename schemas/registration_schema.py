from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class RegistrationBase(BaseModel):
    racer_id: int
    event_id: int
    status: Literal['registered', 'payment_pending', 'cancelled'] = 'registered'

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(BaseModel):
    status: Literal['registered', 'payment_pending', 'cancelled']

class Registration(RegistrationBase):
    id: int
    registration_date: datetime

    class Config:
        orm_mode = True
