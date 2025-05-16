from pydantic import BaseModel
from typing import Optional
from datetime import time

class LeaderboardBase(BaseModel):
    current_position: int                        # renamed
    overall_position: Optional[int] = None       # new field
    racer_id: int
    points: int
    best_lap_time: time
    total_wins: int
    total_podium_finishes: int = 0

class LeaderboardCreate(LeaderboardBase):
    pass

class LeaderboardUpdate(BaseModel):
    current_position: Optional[int] = None
    overall_position: Optional[int] = None
    points: Optional[int] = None
    best_lap_time: Optional[time] = None
    total_wins: Optional[int] = None
    total_podium_finishes: Optional[int] = None

class Leaderboard(LeaderboardBase):
    id: int

    class Config:
        orm_mode = True
