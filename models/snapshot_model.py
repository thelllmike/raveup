from sqlalchemy import Column, Integer, String, Float
from database import Base

class Snapshot(Base):
    __tablename__ = "snapshots"

    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(String(10), unique=True, index=True)
    lap_num = Column(Integer)
    current_position = Column(Integer)
    best_lap_time = Column(Float)
    avg_lap_time = Column(Float)
    pit_stops = Column(Integer)
    tire_age = Column(Integer)
    gap_to_leader = Column(Float)
    sector1_time = Column(Float)
    sector2_time = Column(Float)
    sector3_time = Column(Float)
