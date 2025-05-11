from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.racer import Racer
from schemas.racer_schema import RacerCreate, RacerUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_racer(db: Session, racer_id: int):
    return db.query(Racer).filter(Racer.id == racer_id).first()

def get_racer_by_email(db: Session, email: str):
    return db.query(Racer).filter(Racer.email == email).first()

def get_racers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Racer).offset(skip).limit(limit).all()

def create_racer(db: Session, racer: RacerCreate):
    hashed_pw = get_password_hash(racer.password)
    db_racer = Racer(
        first_name=racer.first_name,
        last_name=racer.last_name,
        date_of_birth=racer.date_of_birth,
        nationality=racer.nationality,
        email=racer.email,
        phone=racer.phone,
        password_hash=hashed_pw,
        racer_type=racer.racer_type,
        racing_team=racer.racing_team,
    )
    db.add(db_racer)
    db.commit()
    db.refresh(db_racer)
    return db_racer

def update_racer(db: Session, db_racer: Racer, racer_update: RacerUpdate):
    data = racer_update.dict(exclude_unset=True)
    if "password" in data:
        db_racer.password_hash = get_password_hash(data.pop("password"))
    for key, val in data.items():
        setattr(db_racer, key, val)
    db.commit()
    db.refresh(db_racer)
    return db_racer

def delete_racer(db: Session, db_racer: Racer):
    db.delete(db_racer)
    db.commit()
