from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class RacerDocumentBase(BaseModel):
    racer_id: int
    document_type: Literal['national_id', 'passport']
    file_path: str

class RacerDocumentCreate(RacerDocumentBase):
    pass

class RacerDocument(RacerDocumentBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True
