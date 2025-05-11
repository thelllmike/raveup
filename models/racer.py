from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Racer(Base):
    __tablename__ = "racers"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    nationality = Column(String(50))
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20))
    password_hash = Column(String(255), nullable=False)
    racer_type = Column(String(50))
    racing_team = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # emergency_contacts = relationship(
    #     "EmergencyContact", back_populates="racer", cascade="all, delete"
    # )
    # documents = relationship(
    #     "RacerDocument", back_populates="racer", cascade="all, delete"
    # )
    # registrations = relationship(
    #     "Registration", back_populates="racer", cascade="all, delete"
    # )
    # leaderboard_entries = relationship(
    #     "Leaderboard", back_populates="racer", cascade="all, delete"
    # )
