from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.document_schema import RacerDocument, RacerDocumentCreate
import crud.document_crud as doc_crud

router = APIRouter()

@router.post("/", response_model=RacerDocument)
def upload_document(d: RacerDocumentCreate, db: Session = Depends(get_db)):
    return doc_crud.create_document(db, d)

@router.get("/racer/{racer_id}", response_model=list[RacerDocument])
def list_documents(racer_id: int, db: Session = Depends(get_db)):
    return doc_crud.get_documents_by_racer(db, racer_id)

@router.get("/{doc_id}", response_model=RacerDocument)
def read_document(doc_id: int, db: Session = Depends(get_db)):
    db_d = doc_crud.get_document(db, doc_id)
    if not db_d:
        raise HTTPException(status_code=404, detail="Document not found")
    return db_d

@router.delete("/{doc_id}", status_code=204)
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    db_d = doc_crud.get_document(db, doc_id)
    if not db_d:
        raise HTTPException(status_code=404, detail="Document not found")
    doc_crud.delete_document(db, db_d)
