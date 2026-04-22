import random
from . import schemas
from ..leads import crud as lead_crud

async def generate_message(db, payload: schemas.SalesMessageIn) -> schemas.SalesMessageOut:
    """Mock – troque por chamada ao modelo fine‑tuned quando houver."""
    msg = (
        f"Olá {payload.nome}, tudo bem? Vi que sua empresa atua no segmento "
        f"{payload.segmento} e demonstra interesse em {payload.interesse}. "
        "Gostaria de marcar uma breve conversa para mostrarmos como nossa solução pode gerar resultados?"
    )
    tom = "persuasivo"
    chance = (
        round(random.uniform(0.7, 0.95), 2)
        if payload.temperatura == "quente"
        else round(random.uniform(0.4, 0.7), 2)
    )
    return schemas.SalesMessageOut(
        mensagem_whatsapp=msg,
        tom=tom,
        chance_fechamento=chance,
    )

async def generate_followup(db, payload: schemas.FollowupIn) -> schemas.FollowupOut:
    lead = await lead_crud.get_lead(db, payload.lead_id)
    if not lead:
        raise ValueError("Lead não encontrado")
    msg = (
        f"Oi {lead.nome}, percebemos que faz um tempo que não ouvimos você. "
        f"Será que ainda tem interesse em {payload.motivo or 'nossos serviços'}?"
    )
    return schemas.FollowupOut(mensagem_whatsapp=msg, tom="educativo")
