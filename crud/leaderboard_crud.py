from sqlalchemy.orm import Session
from models.leaderboard import Leaderboard
from schemas.leaderboard_schema import LeaderboardCreate, LeaderboardUpdate

def get_entry(db: Session, entry_id: int):
    return db.query(Leaderboard).filter(Leaderboard.id == entry_id).first()

def get_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Leaderboard).offset(skip).limit(limit).all()

def create_entry(db: Session, ent: LeaderboardCreate):
    db_ent = Leaderboard(**ent.dict())
    db.add(db_ent)
    db.commit()
    db.refresh(db_ent)
    return db_ent

def update_entry(db: Session, db_ent: Leaderboard, upd: LeaderboardUpdate):
    for k, v in upd.dict(exclude_unset=True).items():
        setattr(db_ent, k, v)
    db.commit()
    db.refresh(db_ent)
    return db_ent

def delete_entry(db: Session, db_ent: Leaderboard):
    db.delete(db_ent)
    db.commit()
