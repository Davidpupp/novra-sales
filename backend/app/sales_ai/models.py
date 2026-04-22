from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from ..db.base import Base

class SalesLog(Base):
    __tablename__ = "sales_logs"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id", ondelete="CASCADE"))
    message = Column(String, nullable=False)
    tone = Column(String(30), nullable=False)
    chance_fechamento = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    lead = relationship("Lead", back_populates="sales_logs")
