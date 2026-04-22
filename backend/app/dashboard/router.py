from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..api.deps import get_current_user
from ..db.session import get_db
from ..db import models
from . import schemas
from ..leads import crud as lead_crud
from ..sales_ai import crud as sales_crud

router = APIRouter(prefix="/v1/dashboard", tags=["dashboard"])

@router.get("/", response_model=schemas.DashboardStats)
async def get_dashboard(
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    total = await lead_crud.count_leads(db)
    quentes = await lead_crud.count_by_status(db, "quente")
    fechadas = await sales_crud.count_closed_sales(db)
    ticket = await sales_crud.avg_ticket(db)

    taxa = (fechadas / total) if total else 0.0
    return schemas.DashboardStats(
        total_leads=total,
        leads_quentes=quentes,
        taxa_conversao=round(taxa, 4),
        vendas_fechadas=fechadas,
        ticket_medio=round(ticket or 0.0, 2),
    )
