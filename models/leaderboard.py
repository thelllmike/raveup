from sqlalchemy import Column, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, index=True)
    rank_position = Column(Integer, unique=True, nullable=False)
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=False)
    points = Column(Integer, nullable=False)
    best_lap_time = Column(Time, nullable=False)
    total_wins = Column(Integer, nullable=False)

    # racer = relationship("Racer", back_populates="leaderboard_entries")
