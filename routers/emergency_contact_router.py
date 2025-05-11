from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.emergency_contact_schema import (
    EmergencyContact,
    EmergencyContactCreate,
    EmergencyContactUpdate,
)
import crud.emergency_contact_crud as ec_crud

router = APIRouter()

@router.post("/", response_model=EmergencyContact)
def create_contact(c: EmergencyContactCreate, db: Session = Depends(get_db)):
    return ec_crud.create_contact(db, c)

@router.get("/racer/{racer_id}", response_model=list[EmergencyContact])
def list_contacts(racer_id: int, db: Session = Depends(get_db)):
    return ec_crud.get_contacts_by_racer(db, racer_id)

@router.get("/{contact_id}", response_model=EmergencyContact)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_c = ec_crud.get_contact(db, contact_id)
    if not db_c:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_c

@router.put("/{contact_id}", response_model=EmergencyContact)
def update_contact(contact_id: int, upd: EmergencyContactUpdate, db: Session = Depends(get_db)):
    db_c = ec_crud.get_contact(db, contact_id)
    if not db_c:
        raise HTTPException(status_code=404, detail="Contact not found")
    return ec_crud.update_contact(db, db_c, upd)

@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_c = ec_crud.get_contact(db, contact_id)
    if not db_c:
        raise HTTPException(status_code=404, detail="Contact not found")
    ec_crud.delete_contact(db, db_c)
