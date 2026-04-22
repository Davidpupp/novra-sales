from fastapi import APIRouter
# Novos módulos:
from app.leads.router import router as leads_router
from app.crm.router import router as crm_router
from app.sales_ai.router import router as sales_router
from app.dashboard.router import router as dashboard_router

router = APIRouter()

router.include_router(leads_router)
router.include_router(crm_router)
router.include_router(sales_router)
router.include_router(dashboard_router)
