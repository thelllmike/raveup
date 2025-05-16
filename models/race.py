from sqlalchemy import Column, Integer, String, Date
from database import Base

class Race(Base):
    __tablename__ = "races"

    id = Column(Integer, primary_key=True, index=True)
    race_name = Column(String(255), nullable=False)           # ✅ Length added
    location = Column(String(255), nullable=False)            # ✅ Length added
    date = Column(Date, nullable=False)
    category = Column(String(100), nullable=False)            # ✅ Length added
    max_participants = Column(Integer, nullable=False)
