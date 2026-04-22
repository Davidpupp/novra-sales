import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import relationship
from ..db.base import Base

class Stage(str, enum.Enum):
    NOVO_LEAD = "novo_lead"
    CONTATO = "contato"
    PROPOSTA = "proposta"
    NEGOCIACAO = "negociacao"
    FECHADO = "fechado"

class CrmNote(Base):
    __tablename__ = "crm_notes"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id", ondelete="CASCADE"))
    stage = Column(Enum(Stage), nullable=False)
    note = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    lead = relationship("Lead", back_populates="crm_notes")
