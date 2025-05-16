from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud.race_crud as race_crud
import schemas.race_schema as schema

router = APIRouter(prefix="/races", tags=["Races"])

@router.post("/", response_model=schema.RaceOut)
def create_race(race: schema.RaceCreate, db: Session = Depends(get_db)):
    return race_crud.create_race(db, race)

@router.get("/", response_model=list[schema.RaceOut])
def get_races(db: Session = Depends(get_db)):
    return race_crud.get_all_races(db)

@router.get("/{race_id}", response_model=schema.RaceOut)
def get_race(race_id: int, db: Session = Depends(get_db)):
    race = race_crud.get_race_by_id(db, race_id)
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    return race

@router.put("/{race_id}", response_model=schema.RaceOut)
def update_race(race_id: int, race_data: schema.RaceUpdate, db: Session = Depends(get_db)):
    updated = race_crud.update_race(db, race_id, race_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Race not found")
    return updated

@router.delete("/{race_id}")
def delete_race(race_id: int, db: Session = Depends(get_db)):
    deleted = race_crud.delete_race(db, race_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Race not found")
    return {"detail": "Race deleted successfully"}
