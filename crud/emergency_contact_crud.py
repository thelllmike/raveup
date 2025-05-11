from sqlalchemy.orm import Session
from models.emergency_contact import EmergencyContact
from schemas.emergency_contact_schema import EmergencyContactCreate, EmergencyContactUpdate

def get_contact(db: Session, contact_id: int):
    return db.query(EmergencyContact).filter(EmergencyContact.id == contact_id).first()

def get_contacts_by_racer(db: Session, racer_id: int):
    return db.query(EmergencyContact).filter(EmergencyContact.racer_id == racer_id).all()

def create_contact(db: Session, contact: EmergencyContactCreate):
    db_contact = EmergencyContact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, db_contact: EmergencyContact, upd: EmergencyContactUpdate):
    for k, v in upd.dict(exclude_unset=True).items():
        setattr(db_contact, k, v)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, db_contact: EmergencyContact):
    db.delete(db_contact)
    db.commit()
