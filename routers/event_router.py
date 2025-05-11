from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.event_schema import EventCreate, EventOut, EventUpdate
import crud.event_crud as ev_crud

router = APIRouter()

@router.post("/", response_model=EventOut)
def create_event(e: EventCreate, db: Session = Depends(get_db)):
    return ev_crud.create_event(db, e)

@router.get("/", response_model=list[EventOut])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ev_crud.get_events(db, skip, limit)

@router.get("/{event_id}", response_model=EventOut)
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_e = ev_crud.get_event(db, event_id)
    if not db_e:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_e

@router.put("/{event_id}", response_model=EventOut)
def update_event(event_id: int, upd: EventUpdate, db: Session = Depends(get_db)):
    db_e = ev_crud.get_event(db, event_id)
    if not db_e:
        raise HTTPException(status_code=404, detail="Event not found")
    return ev_crud.update_event(db, db_e, upd)

@router.delete("/{event_id}", status_code=204)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    db_e = ev_crud.get_event(db, event_id)
    if not db_e:
        raise HTTPException(status_code=404, detail="Event not found")
    ev_crud.delete_event(db, db_e)
