from sqlalchemy.orm import Session
from models.race import Race
from schemas.race_schema import RaceCreate, RaceUpdate

def create_race(db: Session, race: RaceCreate):
    db_race = Race(**race.dict())
    db.add(db_race)
    db.commit()
    db.refresh(db_race)
    return db_race

def get_all_races(db: Session):
    return db.query(Race).all()

def get_race_by_id(db: Session, race_id: int):
    return db.query(Race).filter(Race.id == race_id).first()

def update_race(db: Session, race_id: int, race_update: RaceUpdate):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race:
        for field, value in race_update.dict(exclude_unset=True).items():
            setattr(db_race, field, value)
        db.commit()
        db.refresh(db_race)
    return db_race

def delete_race(db: Session, race_id: int):
    db_race = db.query(Race).filter(Race.id == race_id).first()
    if db_race:
        db.delete(db_race)
        db.commit()
    return db_race
