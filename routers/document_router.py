from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import Literal
import os
import uuid

from database import get_db
from schemas.document_schema import RacerDocument, RacerDocumentCreate
import crud.document_crud as doc_crud

router = APIRouter(prefix="/documents", tags=["documents"])

UPLOAD_DIR = "documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=RacerDocument)
async def upload_document(
    racer_id: int = Form(...),
    document_type: Literal["national_id", "passport"] = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    ext = os.path.splitext(file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    doc_data = RacerDocumentCreate(
        racer_id=racer_id,
        document_type=document_type,
        file_path=file_path
    )
    return doc_crud.create_document(db, doc_data)

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
