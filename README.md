# AI Marketing Intelligence Platform

An autonomous AI marketing platform powered by LangChain, PandasAI, BERTopic, Transformers, Flowise, and Gemini.

## Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React + Tailwind + Framer Motion + Recharts |
| Gateway | FastAPI |
| Orchestration | LangChain Agents |
| Data Cleaning | PandasAI |
| Sentiment | HuggingFace Transformers |
| Trend Detection | BERTopic |
| Forecasting | Prophet |
| Workflows | Flowise |
| Intelligence | Gemini 2.5 Pro |
| Vector Memory | ChromaDB |
| Database | PostgreSQL |
| Cache/Queue | Redis + Celery |

## Quick Start

```bash
# 1. Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-marketing-platform.git
cd ai-marketing-platform

# 2. Set up environment
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# 3. Run with Docker
docker-compose up --build

# 4. Frontend
cd frontend
npm install
npm run dev
```

## Services

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Frontend**: http://localhost:5173
- **Flowise**: http://localhost:3000 (`npx flowise start`)

## Agents

| Agent | Description |
|-------|-------------|
| Cleaning Agent | Auto-cleans uploaded CSV datasets |
| Sentiment Agent | Analyzes emotion in marketing text |
| Trend Agent | Detects viral topics with BERTopic |
| Forecast Agent | Predicts demand and campaign success |
| Report Agent | Generates executive summaries |
| Research Agent | Gathers market intelligence |

## Deployment

**Backend**: Railway / Render / AWS  
**Frontend**: Vercel / Netlify

## License

MIT
