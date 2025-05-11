from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.leaderboard_schema import Leaderboard, LeaderboardCreate, LeaderboardUpdate
import crud.leaderboard_crud as lb_crud

router = APIRouter()

@router.post("/", response_model=Leaderboard)
def create_entry(e: LeaderboardCreate, db: Session = Depends(get_db)):
    return lb_crud.create_entry(db, e)

@router.get("/", response_model=list[Leaderboard])
def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return lb_crud.get_entries(db, skip, limit)

@router.get("/{entry_id}", response_model=Leaderboard)
def read_entry(entry_id: int, db: Session = Depends(get_db)):
    db_e = lb_crud.get_entry(db, entry_id)
    if not db_e:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_e

@router.put("/{entry_id}", response_model=Leaderboard)
def update_entry(entry_id: int, upd: LeaderboardUpdate, db: Session = Depends(get_db)):
    db_e = lb_crud.get_entry(db, entry_id)
    if not db_e:
        raise HTTPException(status_code=404, detail="Entry not found")
    return lb_crud.update_entry(db, db_e, upd)

@router.delete("/{entry_id}", status_code=204)
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db_e = lb_crud.get_entry(db, entry_id)
    if not db_e:
        raise HTTPException(status_code=404, detail="Entry not found")
    lb_crud.delete_entry(db, db_e)
