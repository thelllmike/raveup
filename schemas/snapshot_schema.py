# schemas.py
from pydantic import BaseModel

class SnapshotCreate(BaseModel):
    driver_id        : str
    driver_name      : str           # ← new
    lap_num          : int
    current_position : int
    best_lap_time    : float
    avg_lap_time     : float
    pit_stops        : int
    tire_age         : int
    gap_to_leader    : float
    sector1_time     : float
    sector2_time     : float
    sector3_time     : float

class SnapshotOut(BaseModel):
    driver_id        : str
    driver_name      : str       # ← still required here
    predicted_finish : int
    predicted_rank   : int
    
    class Config:
        orm_mode = True
