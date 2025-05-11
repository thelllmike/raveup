from sqlalchemy.orm import Session
from models.document import RacerDocument
from schemas.document_schema import RacerDocumentCreate

def get_document(db: Session, doc_id: int):
    return db.query(RacerDocument).filter(RacerDocument.id == doc_id).first()

def get_documents_by_racer(db: Session, racer_id: int):
    return db.query(RacerDocument).filter(RacerDocument.racer_id == racer_id).all()

def create_document(db: Session, doc: RacerDocumentCreate):
    db_doc = RacerDocument(**doc.dict())
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc

def delete_document(db: Session, db_doc: RacerDocument):
    db.delete(db_doc)
    db.commit()
