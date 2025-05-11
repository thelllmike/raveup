from sqlalchemy.orm import Session
from models.registration import Registration
from schemas.registration_schema import RegistrationCreate, RegistrationUpdate

def get_registration(db: Session, reg_id: int):
    return db.query(Registration).filter(Registration.id == reg_id).first()

def get_registrations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Registration).offset(skip).limit(limit).all()

def get_registrations_by_racer(db: Session, racer_id: int):
    return db.query(Registration).filter(Registration.racer_id == racer_id).all()

def create_registration(db: Session, reg: RegistrationCreate):
    db_reg = Registration(**reg.dict())
    db.add(db_reg)
    db.commit()
    db.refresh(db_reg)
    return db_reg

def update_registration(db: Session, db_reg: Registration, upd: RegistrationUpdate):
    for k, v in upd.dict(exclude_unset=True).items():
        setattr(db_reg, k, v)
    db.commit()
    db.refresh(db_reg)
    return db_reg

def delete_registration(db: Session, db_reg: Registration):
    db.delete(db_reg)
    db.commit()
