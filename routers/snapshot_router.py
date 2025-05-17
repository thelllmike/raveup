from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.snapshot_schema import SnapshotCreate, SnapshotOut
from crud.snapshot_crud import upsert_snapshot, get_all_snapshots
from database import get_db
from models.snapshot_model import Snapshot

import pandas as pd
import joblib
import os
import numpy as np

router = APIRouter(prefix="/snapshots", tags=["Race Snapshots"])

# Load updated ML model and scaler
model_path = os.path.join("model", "rf_ranker_improved.joblib")
scaler_path = os.path.join("model", "rf_scaler_improved.joblib")
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

features = [
    "lap_num", "current_position", "avg_lap_time",
    "pit_stops", "tire_age", "gap_to_leader",
    "sector1_time", "sector2_time", "sector3_time", "inv_best_lap"
]

@router.post("/submit", response_model=SnapshotOut)
def submit_snapshot(data: SnapshotCreate, db: Session = Depends(get_db)):
    upsert_snapshot(db, data)
    return predict_all_snapshots(db)[-1]  # Return last added driver

@router.get("/rankings", response_model=list[SnapshotOut])
def get_rankings(db: Session = Depends(get_db)):
    return predict_all_snapshots(db)

def predict_all_snapshots(db: Session):
    entries = get_all_snapshots(db)
    if not entries:
        raise HTTPException(status_code=404, detail="No snapshot data found")

    df = pd.DataFrame([e.__dict__ for e in entries])
    df.drop(columns=["_sa_instance_state", "id"], inplace=True)
    df["inv_best_lap"] = -df["best_lap_time"]

    scaled = scaler.transform(df[features])
    df["predicted_finish"] = np.round(model.predict(scaled)).astype(int)

    # Tie-breaker: sort by predicted_finish then current_position
    df = df.sort_values(by=["predicted_finish", "current_position"], ascending=[True, True]).reset_index(drop=True)

    # Assign proper sequential ranking
    df["predicted_rank"] = np.arange(1, len(df) + 1)

    return [
        SnapshotOut(driver_id=row["driver_id"],
                    predicted_finish=row["predicted_finish"],
                    predicted_rank=row["predicted_rank"])
        for _, row in df.iterrows()
    ]


@router.put("/update/{driver_id}", response_model=SnapshotOut)
def update_snapshot_data(
    driver_id: str,
    data: SnapshotCreate,
    db: Session = Depends(get_db)
):
    try:
        from crud.snapshot_crud import update_snapshot
        update_snapshot(db, driver_id, data)
        return predict_all_snapshots(db)[-1]  # Return updated driver's prediction
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))