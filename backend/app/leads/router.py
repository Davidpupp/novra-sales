from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..api.deps import get_current_user
from ..db.session import get_db
from ..db import models
from . import crud, schemas

router = APIRouter(prefix="/v1/leads", tags=["leads"])

@router.post("/", response_model=schemas.LeadRead, status_code=201)
async def create_lead(
    payload: schemas.LeadCreate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await crud.create_lead(db, payload)

@router.get("/", response_model=list[schemas.LeadRead])
async def list_leads(
    status: schemas.LeadStatus | None = None,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await crud.get_leads(db, status)

@router.put("/{lead_id}", response_model=schemas.LeadRead)
async def edit_lead(
    lead_id: int,
    payload: schemas.LeadUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await crud.update_lead(db, lead_id, payload)

@router.delete("/{lead_id}", status_code=204)
async def delete_lead(
    lead_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    await crud.delete_lead(db, lead_id)
    return None
