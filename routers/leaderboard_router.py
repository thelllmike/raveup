# routers/leaderboard_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import crud.leaderboard_crud as crud
from schemas.leaderboard_schema import Leaderboard, LeaderboardCreate, LeaderboardUpdate

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

@router.get("/", response_model=List[Leaderboard])
def read_leaderboard(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_entries(db, skip=skip, limit=limit)

@router.get("/racer/{racer_id}", response_model=List[Leaderboard])
def read_leaderboard_by_racer(
    racer_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    entries = crud.get_entries_by_racer(db, racer_id, skip=skip, limit=limit)
    if not entries:
        # It might be normal to have zero entries, but if you want to 404 on no records:
        # raise HTTPException(status_code=404, detail="No leaderboard entries found for this racer")
        return []
    return entries

@router.post("/", response_model=Leaderboard)
def create_leaderboard_entry(
    entry: LeaderboardCreate,
    db: Session = Depends(get_db)
):
    return crud.create_entry(db, entry)

@router.patch("/{entry_id}", response_model=Leaderboard)
def update_leaderboard_entry(
    entry_id: int,
    upd: LeaderboardUpdate,
    db: Session = Depends(get_db)
):
    db_ent = crud.get_entry(db, entry_id)
    if not db_ent:
        raise HTTPException(status_code=404, detail="Entry not found")
    return crud.update_entry(db, db_ent, upd)

@router.delete("/{entry_id}", status_code=204)
def delete_leaderboard_entry(
    entry_id: int,
    db: Session = Depends(get_db)
):
    db_ent = crud.get_entry(db, entry_id)
    if not db_ent:
        raise HTTPException(status_code=404, detail="Entry not found")
    crud.delete_entry(db, db_ent)
