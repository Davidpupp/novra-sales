from enum import Enum
from pydantic import BaseModel, Field

class Temperature(str, Enum):
    QUENTE = "quente"
    MORNO = "morno"
    FRIO = "frio"
    FECHADO = "fechado"

class SalesMessageIn(BaseModel):
    nome: str
    segmento: str
    interesse: str
    temperatura: Temperature

class SalesMessageOut(BaseModel):
    mensagem_whatsapp: str
    tom: str = Field(..., description="Tom da mensagem (ex.: persuasivo, educativo)")
    chance_fechamento: float = Field(..., ge=0, le=1)

class FollowupIn(BaseModel):
    lead_id: int
    motivo: str | None = None

class FollowupOut(BaseModel):
    mensagem_whatsapp: str
    tom: str
