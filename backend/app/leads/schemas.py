from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class LeadStatus(str, Enum):
    QUENTE = "quente"
    MORNO = "morno"
    FRIO = "frio"
    FECHADO = "fechado"

class TagSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class LeadBase(BaseModel):
    nome: str = Field(..., max_length=120)
    whatsapp: str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")
    origem: Optional[str] = None
    status: LeadStatus = LeadStatus.FRIO
    tags: Optional[List[int]] = []

class LeadCreate(LeadBase):
    pass

class LeadUpdate(BaseModel):
    nome: Optional[str] = None
    whatsapp: Optional[str] = None
    origem: Optional[str] = None
    status: Optional[LeadStatus] = None
    tags: Optional[List[int]] = None

class LeadRead(LeadBase):
    id: int
    created_at: datetime
    tags: List[TagSchema] = []

    class Config:
        orm_mode = True
