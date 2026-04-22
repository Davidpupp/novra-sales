from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from . import models, schemas

async def create_lead(db: AsyncSession, payload: schemas.LeadCreate) -> models.Lead:
    new = models.Lead(**payload.dict())
    db.add(new)
    await db.commit()
    await db.refresh(new)
    return new

async def get_lead(db: AsyncSession, lead_id: int) -> models.Lead | None:
    result = await db.execute(select(models.Lead).where(models.Lead.id == lead_id))
    return result.scalar_one_or_none()

async def get_lead_by_whatsapp(db: AsyncSession, whatsapp: str) -> models.Lead | None:
    result = await db.execute(select(models.Lead).where(models.Lead.whatsapp == whatsapp))
    return result.scalar_one_or_none()

async def get_leads(db: AsyncSession, status: schemas.LeadStatus | None = None):
    stmt = select(models.Lead).order_by(models.Lead.created_at.desc())
    if status:
        stmt = stmt.where(models.Lead.status == status)
    result = await db.execute(stmt)
    return result.scalars().all()

async def update_lead(db: AsyncSession, lead_id: int, payload: schemas.LeadUpdate):
    stmt = (
        update(models.Lead)
        .where(models.Lead.id == lead_id)
        .values(**payload.dict(exclude_unset=True))
        .execution_options(synchronize_session="fetch")
    )
    await db.execute(stmt)
    await db.commit()
    lead = await get_lead(db, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

async def delete_lead(db: AsyncSession, lead_id: int):
    await db.execute(delete(models.Lead).where(models.Lead.id == lead_id))
    await db.commit()

# Métricas usadas no dashboard
async def count_leads(db: AsyncSession) -> int:
    result = await db.execute(select(func.count()).select_from(models.Lead))
    return result.scalar_one()

async def count_by_status(db: AsyncSession, status: str) -> int:
    result = await db.execute(select(func.count()).select_from(models.Lead).where(models.Lead.status == status))
    return result.scalar_one()
