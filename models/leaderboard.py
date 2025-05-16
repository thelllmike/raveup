from sqlalchemy import Column, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, index=True)
    current_position = Column(Integer, unique=True, nullable=False)  # renamed from rank_position
    overall_position = Column(Integer, nullable=True)  # new field
    racer_id = Column(Integer, ForeignKey("racers.id", ondelete="CASCADE"), nullable=False)
    points = Column(Integer, nullable=False)
    best_lap_time = Column(Time, nullable=False)
    total_wins = Column(Integer, nullable=False)
    total_podium_finishes = Column(Integer, nullable=False, default=0)
