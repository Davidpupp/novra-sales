from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..api.deps import get_current_user
from ..db.session import get_db
from ..db import models
from . import schemas, services

router = APIRouter(prefix="/v1/sales", tags=["sales_ai"])

@router.post("/generate-message", response_model=schemas.SalesMessageOut)
async def generate_message(
    payload: schemas.SalesMessageIn,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await services.generate_message(db, payload)

@router.post("/followup", response_model=schemas.FollowupOut)
async def followup(
    payload: schemas.FollowupIn,
    db: AsyncSession = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return await services.generate_followup(db, payload)
