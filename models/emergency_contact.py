from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=False)
    contact_name = Column(String(100), nullable=False)
    relationship = Column(String(50))
    contact_phone = Column(String(20))

    # racer = relationship("Racer", back_populates="emergency_contacts")
