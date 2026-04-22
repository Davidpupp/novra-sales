# ---------- Build do frontend ----------
FROM node:20-alpine AS ui-builder
WORKDIR /ui
COPY frontend/ .
RUN npm ci && npm run build

# ---------- Imagem final ----------
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN ls -la /app/
COPY backend/ .
COPY --from=ui-builder /ui/static /app/static
RUN pip install --no-cache-dir -r requirements.txt

ENV DATABASE_URL=postgresql+asyncpg://postgres:postgres@db/novra
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
