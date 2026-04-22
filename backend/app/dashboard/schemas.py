from pydantic import BaseModel

class DashboardStats(BaseModel):
    total_leads: int
    leads_quentes: int
    taxa_conversao: float
    vendas_fechadas: int
    ticket_medio: float
