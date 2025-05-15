from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base
import enum

class DocumentType(enum.Enum):
    national_id = "national_id"
    passport = "passport"
    image = "image"

class RacerDocument(Base):
    __tablename__ = "racer_documents"

    id = Column(Integer, primary_key=True, index=True)
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=False)
    document_type = Column(Enum(DocumentType), nullable=False)
    file_path = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    # racer = relationship("Racer", back_populates="documents")
