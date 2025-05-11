from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    event_date = Column(Date, nullable=False)
    location = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)

    # registrations = relationship("Registration", back_populates="event", cascade="all, delete")
