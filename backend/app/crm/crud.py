from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from . import models, schemas

async def create_note(db: AsyncSession, payload: schemas.CrmNoteCreate) -> models.CrmNote:
    stmt = insert(models.CrmNote).values(**payload.dict())
    result = await db.execute(stmt)
    await db.commit()
    note_id = result.inserted_primary_key[0]
    note = await db.get(models.CrmNote, note_id)
    return note

async def get_notes_by_lead(db: AsyncSession, lead_id: int) -> list[models.CrmNote]:
    stmt = select(models.CrmNote).where(models.CrmNote.lead_id == lead_id).order_by(models.CrmNote.created_at.desc())
    result = await db.execute(stmt)
    return result.scalars().all()
