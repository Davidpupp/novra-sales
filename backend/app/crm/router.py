from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..api.deps import get_current_user
from ..db.session import get_db
from ..db import models
from . import crud, schemas

router = APIRouter(prefix="/v1/crm", tags=["crm"])

@router.post("/note", response_model=schemas.CrmNoteRead)
async def add_note(
    payload: schemas.CrmNoteCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await crud.create_note(db, payload)

@router.get("/lead/{lead_id}/notes", response_model=list[schemas.CrmNoteRead])
async def list_notes(
    lead_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await crud.get_notes_by_lead(db, lead_id)
