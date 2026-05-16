# CLAUDE.md — AI Marketing Intelligence Platform

This file briefs Claude Code on the full project. Read it entirely before taking any action.

---

## Project Goal

Build an **Autonomous AI Marketing Intelligence Platform** that:
- Collects marketing/social data
- Cleans datasets automatically via PandasAI
- Analyzes sentiment via Transformers
- Discovers trends via BERTopic
- Forecasts patterns via a forecasting engine
- Orchestrates autonomous agents via LangChain + Flowise
- Presents everything in a React dashboard

---

## Architecture

```
Frontend (React + Tailwind + Framer Motion + Recharts)
            ↓
      FastAPI Gateway  (port 8000)
            ↓
    LangChain Orchestrator
            ↓
 ┌──────────┼──────────┐
 ↓          ↓          ↓
PandasAI  Flowise   NLP Engine
Cleaning  Workflow  Transformers
            ↓
      BERTopic Engine
            ↓
      Forecast Engine
            ↓
  PostgreSQL + ChromaDB + Redis
```

---

## Monorepo Structure

```
ai-marketing-platform/
├── frontend/
│   ├── app/                  # Next.js app router or Vite entry
│   ├── components/           # Reusable UI components
│   ├── dashboard/            # Dashboard pages
│   └── analytics/            # Charts and analytics views
├── backend/
│   ├── main.py               # FastAPI entry point
│   ├── api/
│   │   └── routes.py         # All API routes
│   ├── orchestration/
│   │   └── agent_controller.py
│   ├── agents/               # Individual agent definitions
│   ├── workflows/            # LangChain workflow chains
│   ├── memory/
│   │   └── vector_store.py   # ChromaDB integration
│   └── services/
│       └── gemini_service.py
├── services/
│   ├── pandasai_service/
│   │   └── cleaner.py
│   ├── langchain_service/
│   ├── flowise_service/
│   ├── sentiment_service/
│   │   └── analyzer.py
│   ├── bertopic_service/
│   │   └── topics.py
│   └── forecasting_service/
│       └── forecaster.py
├── infrastructure/
│   ├── docker/
│   ├── kubernetes/
│   └── terraform/
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## Environment Variables

Always read from `.env`. Never hardcode secrets. Create `.env.example` with:

```
GOOGLE_API_KEY=your_gemini_key_here
POSTGRES_URL=postgresql://user:pass@localhost:5432/marketing
REDIS_URL=redis://localhost:6379
CHROMA_HOST=localhost
CHROMA_PORT=8001
```

---

## Build Phases — Execute in Order

### Phase 1 — Core Backend
1. Create `backend/main.py` FastAPI app
2. Create `backend/services/gemini_service.py` with Gemini 2.5 Pro
3. Create `services/pandasai_service/cleaner.py`
4. Create `backend/api/routes.py` with `/clean`, `/health` endpoints
5. Create `requirements.txt` with all dependencies
6. Create `.env.example`

### Phase 2 — Orchestration + Memory
7. Create `backend/orchestration/agent_controller.py` (LangChain agents)
8. Create `backend/memory/vector_store.py` (ChromaDB)
9. Add `/analyze`, `/memory/save`, `/memory/query` routes

### Phase 3 — NLP Engines
10. Create `services/sentiment_service/analyzer.py` (HuggingFace Transformers)
11. Create `services/bertopic_service/topics.py` (BERTopic)
12. Add `/sentiment`, `/topics` routes

### Phase 4 — Forecasting + Flowise
13. Create `services/forecasting_service/forecaster.py` (Prophet + fallback)
14. Add `/forecast` route
15. Create `services/flowise_service/client.py` (Flowise HTTP client)
16. Add Flowise webhook route

### Phase 5 — Frontend Dashboard
17. Scaffold React frontend with Vite + Tailwind
18. Build dashboard with sentiment charts, trend graphs, AI insights panel
19. Connect all frontend pages to FastAPI endpoints
20. Add Framer Motion animations and Recharts visualizations

### Phase 6 — Infrastructure
21. Create `Dockerfile` for backend
22. Create `docker-compose.yml` (api + postgres + redis + chromadb)
23. Create `README.md` with full setup instructions

---

## Agents to Implement

| Agent | File | Responsibility |
|-------|------|----------------|
| Cleaning Agent | `agents/cleaning_agent.py` | Auto-clean uploaded CSVs |
| Sentiment Agent | `agents/sentiment_agent.py` | Analyze text emotion |
| Trend Agent | `agents/trend_agent.py` | Detect viral topics |
| Forecast Agent | `agents/forecast_agent.py` | Predict future patterns |
| Report Agent | `agents/report_agent.py` | Generate markdown reports |
| Research Agent | `agents/research_agent.py` | Gather market intelligence |

---

## API Endpoints (Full List)

```
POST /clean              — Upload CSV, returns cleaning summary
POST /sentiment          — Analyze sentiment of text input
POST /topics             — Detect BERTopic topics from documents
POST /forecast           — Forecast time series data
POST /analyze            — LangChain orchestrated full analysis
POST /memory/save        — Save context to ChromaDB
POST /memory/query       — Query ChromaDB vector memory
GET  /health             — Health check
GET  /agents             — List available agents
POST /agents/{name}/run  — Run a specific agent
```

---

## Code Standards

- **Python**: Use type hints everywhere. Async FastAPI endpoints. Pydantic models for all request/response bodies.
- **Error handling**: Every service must have try/except with meaningful error messages returned as JSON.
- **Logging**: Use Python `logging` module, not print statements.
- **Frontend**: Functional React components only. No class components. Use hooks.
- **Styling**: Tailwind utility classes only. No inline styles except for dynamic values.

---

## Key Dependencies

```txt
# Backend
fastapi
uvicorn[standard]
pandas
numpy
langchain
langchain-google-genai
google-generativeai
pandasai
transformers
sentence-transformers
bertopic
scikit-learn
chromadb
sqlalchemy
psycopg2-binary
redis
celery
python-dotenv
prophet
httpx
pydantic

# Frontend (package.json)
react, react-dom
vite
tailwindcss
framer-motion
recharts
axios
```

---

## Git Workflow

After completing each phase:
```bash
git add .
git commit -m "phase X: description of what was built"
git push origin main
```

Commit messages should be descriptive. One commit per phase minimum.

---

## What NOT to Do

- Do not use `print()` — use `logging`
- Do not hardcode API keys
- Do not create monolithic files — keep services modular
- Do not skip error handling
- Do not use class components in React
- Do not commit `.env` files (only `.env.example`)

---

## Start Command

When ready, Claude Code should begin with Phase 1 and work sequentially through all phases, committing after each phase completes. Ask for clarification only if a phase requirement is genuinely ambiguous.
