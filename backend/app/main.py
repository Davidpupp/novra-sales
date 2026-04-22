"""Pacote principal da aplicação NOVRA Sales AI."""

import logging
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.router import router as api_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

app = FastAPI(
    title="NOVRA AI Decision Engine",
    version="0.1.0",
    description="MVP de decisão assistida por IA – FastAPI + JWT + SQLite/PG",
)

app.include_router(api_router, prefix="/api")
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
