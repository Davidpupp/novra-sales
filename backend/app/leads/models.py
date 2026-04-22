import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum, Table, ForeignKey, func
from sqlalchemy.orm import relationship
from ..db.base import Base

class LeadStatus(str, enum.Enum):
    QUENTE = "quente"
    MORNO = "morno"
    FRIO = "frio"
    FECHADO = "fechado"

lead_tag = Table(
    "lead_tag",
    Base.metadata,
    Column("lead_id", Integer, ForeignKey("leads.id", ondelete="CASCADE")),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE")),
)

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False, index=True)
    whatsapp = Column(String(30), nullable=False, unique=True, index=True)
    origem = Column(String(80), nullable=True)
    status = Column(Enum(LeadStatus), default=LeadStatus.FRIO, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    tags = relationship("Tag", secondary=lead_tag, back_populates="leads")
    sales_logs = relationship("SalesLog", back_populates="lead", cascade="all, delete-orphan")
    crm_notes = relationship("CrmNote", back_populates="lead", cascade="all, delete-orphan")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), unique=True, nullable=False)

    leads = relationship("Lead", secondary=lead_tag, back_populates="tags")
