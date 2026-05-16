from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Import the router from backend.api (created below)
from backend.api.routes import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Marketing Intelligence Platform",
    description="Autonomous AI marketing analysis platform",
    version="1.0.0",
)

# CORS Configuration - restrict origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:3000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    max_age=600,
)

app.include_router(router)


@app.get("/health")
async def health():
    return {"status": "online", "message": "AI Marketing Platform running"}
