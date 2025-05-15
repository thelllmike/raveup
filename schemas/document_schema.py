from pydantic import BaseModel
from typing import Literal
from datetime import datetime
from enum import Enum

class DocumentType(str, Enum):
    national_id = 'national_id'
    passport = 'passport'

class RacerDocumentBase(BaseModel):
    racer_id: int
    document_type: DocumentType   # ✅ Use Enum instead of Literal
    file_path: str

class RacerDocumentCreate(RacerDocumentBase):
    pass

class RacerDocument(RacerDocumentBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
        use_enum_values = True  # ✅ ensures enum is returned as string
