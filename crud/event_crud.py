from sqlalchemy.orm import Session
from models.event import Event
from schemas.event_schema import EventCreate, EventUpdate

def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()

def get_events(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()

def create_event(db: Session, ev: EventCreate):
    db_ev = Event(**ev.dict())
    db.add(db_ev)
    db.commit()
    db.refresh(db_ev)
    return db_ev

def update_event(db: Session, db_ev: Event, upd: EventUpdate):
    for k, v in upd.dict(exclude_unset=True).items():
        setattr(db_ev, k, v)
    db.commit()
    db.refresh(db_ev)
    return db_ev

def delete_event(db: Session, db_ev: Event):
    db.delete(db_ev)
    db.commit()
