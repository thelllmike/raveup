from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.snapshot_schema import SnapshotCreate, SnapshotOut
from crud.snapshot_crud import upsert_snapshot, get_all_snapshots
from database import get_db

import pandas as pd
import joblib
import os
import numpy as np

router = APIRouter(prefix="/snapshots", tags=["Race Snapshots"])

model_path  = os.path.join("model", "rf_ranker_improved.joblib")
scaler_path = os.path.join("model", "rf_scaler_improved.joblib")
model  = joblib.load(model_path)
scaler = joblib.load(scaler_path)

features = [
    "lap_num", "current_position", "avg_lap_time",
    "pit_stops", "tire_age", "gap_to_leader",
    "sector1_time", "sector2_time", "sector3_time", "inv_best_lap"
]

@router.post("/submit", response_model=SnapshotOut)
def submit_snapshot(data: SnapshotCreate, db: Session = Depends(get_db)):
    # insert or update the snapshot row (including driver_name)
    upsert_snapshot(db, data)
    # recompute predictions and return the last one
    return predict_all_snapshots(db)[-1]

@router.get("/rankings", response_model=list[SnapshotOut])
def get_rankings(db: Session = Depends(get_db)):
    return predict_all_snapshots(db)

def predict_all_snapshots(db: Session):
    entries = get_all_snapshots(db)
    if not entries:
        raise HTTPException(status_code=404, detail="No snapshot data found")

    # build DataFrame
    df = pd.DataFrame([e.__dict__ for e in entries])
    df.drop(columns=["_sa_instance_state", "id"], inplace=True)
    df["inv_best_lap"] = -df["best_lap_time"]

    # scale & predict
    scaled = scaler.transform(df[features])
    df["predicted_finish"] = np.round(model.predict(scaled)).astype(int)

    # sort + rank
    df = df.sort_values(
        by=["predicted_finish", "current_position"],
        ascending=[True, True]
    ).reset_index(drop=True)
    df["predicted_rank"] = np.arange(1, len(df) + 1)

    # return a list of SnapshotOut, now including driver_name
    return [
        SnapshotOut(
            driver_id        = row["driver_id"],
            driver_name      = row["driver_name"],        # ← include this
            predicted_finish = int(row["predicted_finish"]),
            predicted_rank   = int(row["predicted_rank"])
        )
        for _, row in df.iterrows()
    ]

@router.put("/update/{driver_id}", response_model=SnapshotOut)
def update_snapshot_data(
    driver_id: str,
    data: SnapshotCreate,
    db: Session = Depends(get_db)
):
    from crud.snapshot_crud import update_snapshot

    try:
        update_snapshot(db, driver_id, data)
        return predict_all_snapshots(db)[-1]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
