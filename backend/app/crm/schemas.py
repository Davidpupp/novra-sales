from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class Stage(str, Enum):
    NOVO_LEAD = "novo_lead"
    CONTATO = "contato"
    PROPOSTA = "proposta"
    NEGOCIACAO = "negociacao"
    FECHADO = "fechado"

class CrmNoteCreate(BaseModel):
    lead_id: int
    stage: Stage
    note: str = Field(..., min_length=1)

class CrmNoteRead(CrmNoteCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
