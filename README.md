# NOVRA Sales AI

SaaS de vendas automatizado com IA - FastAPI + PostgreSQL + React + TypeScript.

## Stack

- **Backend:** FastAPI, SQLAlchemy 2.0 (async), Alembic, JWT, PostgreSQL/SQLite
- **Frontend:** React 18, TypeScript, Vite, TailwindCSS, react-beautiful-dnd
- **Deploy:** Docker + Docker Compose (Railway-ready)

## Estrutura

```
novra-sales-ai/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── core/           # Config, segurança
│   │   ├── db/             # Models, session, base
│   │   ├── api/            # Routers, deps
│   │   ├── leads/          # Módulo Leads
│   │   ├── crm/            # Módulo CRM
│   │   ├── sales_ai/       # IA de Vendas
│   │   └── dashboard/      # Métricas
│   └── alembic/            # Migrations
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       └── routes/
└── docker-compose.yml
```

## Instalação Local

### 1. Backend

```bash
cd backend
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r ../requirements.txt

# Configurar env
copy ..\.env.example ..\.env
# Edite .env com sua SECRET_KEY e DATABASE_URL

# Migrations
alembic upgrade head

# Run
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000  
Swagger: http://127.0.0.1:8000/docs

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173  
(Proxy já configura /api → localhost:8000)

## Docker (Produção)

```bash
docker compose up --build -d
docker compose exec api alembic upgrade head
```

Aplicação: http://localhost:8000

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| SECRET_KEY | Chave JWT | obrigatório |
| DATABASE_URL | URL do banco | SQLite (dev) |
| OPENAI_API_KEY | API da OpenAI (opcional) | - |

## Módulos

- **Leads:** CRUD de prospects, tags, status (quente/morno/frio/fechado)
- **CRM:** Pipeline Kanban, notas por estágio
- **Sales AI:** Geração de mensagens WhatsApp, follow-up automático
- **Dashboard:** Métricas consolidadas (conversão, ticket médio)

## Licença

Proprietary - NOVRA Systems
