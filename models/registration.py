# models/registration.py
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.types import Enum as SQLEnum
from sqlalchemy.orm import relationship
from database import Base

class RegistrationStatus(PyEnum):
    registered = "registered"
    payment_pending = "payment_pending"
    cancelled = "cancelled"

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)

    status = Column(
        SQLEnum(RegistrationStatus, name="registration_status"),
        nullable=False,
        server_default=RegistrationStatus.registered.value
    )

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # racer = relationship("Racer", back_populates="registrations")
    # event = relationship("Event", back_populates="registrations")
    event = relationship("Event", back_populates="registrations")
