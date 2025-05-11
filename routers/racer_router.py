from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.racer_schema import RacerCreate, RacerOut, RacerUpdate
import crud.racer_crud as racer_crud

router = APIRouter()

@router.post("/", response_model=RacerOut)
def create_racer(r: RacerCreate, db: Session = Depends(get_db)):
    if racer_crud.get_racer_by_email(db, r.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return racer_crud.create_racer(db, r)

@router.get("/", response_model=list[RacerOut])
def read_racers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return racer_crud.get_racers(db, skip, limit)

@router.get("/{racer_id}", response_model=RacerOut)
def read_racer(racer_id: int, db: Session = Depends(get_db)):
    db_r = racer_crud.get_racer(db, racer_id)
    if not db_r:
        raise HTTPException(status_code=404, detail="Racer not found")
    return db_r

@router.put("/{racer_id}", response_model=RacerOut)
def update_racer(racer_id: int, upd: RacerUpdate, db: Session = Depends(get_db)):
    db_r = racer_crud.get_racer(db, racer_id)
    if not db_r:
        raise HTTPException(status_code=404, detail="Racer not found")
    return racer_crud.update_racer(db, db_r, upd)

@router.delete("/{racer_id}", status_code=204)
def delete_racer(racer_id: int, db: Session = Depends(get_db)):
    db_r = racer_crud.get_racer(db, racer_id)
    if not db_r:
        raise HTTPException(status_code=404, detail="Racer not found")
    racer_crud.delete_racer(db, db_r)
