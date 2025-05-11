import enum
from sqlalchemy import Column, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class RegistrationStatus(enum.Enum):
    registered = "registered"
    payment_pending = "payment_pending"
    cancelled = "cancelled"

class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    status = Column(Enum(RegistrationStatus), nullable=False, default=RegistrationStatus.registered)
    registration_date = Column(DateTime(timezone=True), server_default=func.now())

    # racer = relationship("Racer", back_populates="registrations")
    # event = relationship("Event", back_populates="registrations")
