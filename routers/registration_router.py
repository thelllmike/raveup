from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.registration_schema import Registration, RegistrationCreate, RegistrationUpdate
import crud.registration_crud as reg_crud

router = APIRouter()

@router.post("/", response_model=Registration)
def create_registration(r: RegistrationCreate, db: Session = Depends(get_db)):
    return reg_crud.create_registration(db, r)

@router.get("/", response_model=list[Registration])
def read_registrations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return reg_crud.get_registrations(db, skip, limit)

@router.get("/{reg_id}", response_model=Registration)
def read_registration(reg_id: int, db: Session = Depends(get_db)):
    db_r = reg_crud.get_registration(db, reg_id)
    if not db_r:
        raise HTTPException(status_code=404, detail="Registration not found")
    return db_r

@router.put("/{reg_id}", response_model=Registration)
def update_registration(reg_id: int, upd: RegistrationUpdate, db: Session = Depends(get_db)):
    db_r = reg_crud.get_registration(db, reg_id)
    if not db_r:
        raise HTTPException(status_code=404, detail="Registration not found")
    return reg_crud.update_registration(db, db_r, upd)

@router.delete("/{reg_id}", status_code=204)
def delete_registration(reg_id: int, db: Session = Depends(get_db)):
    db_r = reg_crud.get_registration(db, reg_id)
    if not db_r:
        raise HTTPException(status_code=404, detail="Registration not found")
    reg_crud.delete_registration(db, db_r)
