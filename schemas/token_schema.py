# schemas/token_schema.py
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str  # e.g. "bearer"
    user_id: int  

class TokenData(BaseModel):
    email: str | None = None
