import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY") or (
        lambda: sys.exit("❌ ENV SECRET_KEY não configurada") )()
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./novra.db")
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

settings = Settings()
