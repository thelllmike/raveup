from sqlalchemy.orm import Session
from models.snapshot_model import Snapshot
from schemas.snapshot_schema import SnapshotCreate
from sqlalchemy.exc import NoResultFound

def upsert_snapshot(db: Session, data: SnapshotCreate):
    existing = db.query(Snapshot).filter(Snapshot.driver_id == data.driver_id).first()
    if existing:
        for key, value in data.dict().items():
            setattr(existing, key, value)
    else:
        new_entry = Snapshot(**data.dict())
        db.add(new_entry)
    db.commit()

def get_all_snapshots(db: Session):
    return db.query(Snapshot).all()

def update_snapshot(db: Session, driver_id: str, data: SnapshotCreate):
    snapshot = db.query(Snapshot).filter(Snapshot.driver_id == driver_id).first()
    if not snapshot:
        raise NoResultFound(f"No snapshot found for driver_id: {driver_id}")
    
    for key, value in data.dict().items():
        setattr(snapshot, key, value)

    db.commit()
    return snapshot
