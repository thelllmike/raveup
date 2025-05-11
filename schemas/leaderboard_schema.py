from pydantic import BaseModel
from typing import Optional
from datetime import time

class LeaderboardBase(BaseModel):
    rank_position: int
    racer_id: int
    points: int
    best_lap_time: time
    total_wins: int

class LeaderboardCreate(LeaderboardBase):
    pass

class LeaderboardUpdate(BaseModel):
    rank_position: Optional[int]
    points: Optional[int]
    best_lap_time: Optional[time]
    total_wins: Optional[int]

class Leaderboard(LeaderboardBase):
    id: int

    class Config:
        orm_mode = True
