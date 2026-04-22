from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from .models import SalesLog

async def count_closed_sales(db: AsyncSession) -> int:
    stmt = select(func.count()).select_from(SalesLog).where(SalesLog.chance_fechamento >= 0.7)
    result = await db.execute(stmt)
    return result.scalar_one()

async def avg_ticket(db: AsyncSession) -> float | None:
    stmt = select(func.avg(SalesLog.chance_fechamento * 1000))
    result = await db.execute(stmt)
    return result.scalar_one()
