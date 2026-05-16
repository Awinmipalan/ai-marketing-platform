from fastapi import APIRouter, HTTPException, UploadFile, File, Body
from pydantic import BaseModel
from typing import List, Any, Dict
import logging

# Local service imports (stubs implemented in repo)
from backend.services import gemini_service
from services.pandasai_service import cleaner as pandasai_cleaner
from services.sentiment_service import analyzer as sentiment_analyzer
from services.bertopic_service import topics as bertopic_service
from services.forecasting_service import forecaster as forecasting_service
from backend.memory import vector_store
from backend.orchestration import agent_controller

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["analytics"])


class MessageResponse(BaseModel):
    status: str
    message: str
    data: Dict[str, Any] = {}


class SentimentRequest(BaseModel):
    text: str


class TopicsRequest(BaseModel):
    documents: List[str]


class ForecastRequest(BaseModel):
    data: List[float]


@router.get("/agents")
async def list_agents():
    agents = agent_controller.list_agents()
    return MessageResponse(status="success", message="Agents listed", data={"agents": agents})


@router.post("/clean")
async def clean_data(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = pandasai_cleaner.clean_csv_bytes(contents)
        return MessageResponse(status="success", message="Data cleaned", data={"summary": result})
    except Exception as e:
        logger.exception("Cleaning error")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/sentiment")
async def analyze_sentiment(req: SentimentRequest):
    try:
        result = sentiment_analyzer.analyze_text(req.text)
        return MessageResponse(status="success", message="Sentiment analyzed", data={"sentiment": result})
    except Exception as e:
        logger.exception("Sentiment error")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/topics")
async def detect_topics(req: TopicsRequest):
    try:
        result = bertopic_service.detect_topics(req.documents)
        return MessageResponse(status="success", message="Topics detected", data={"topics": result})
    except Exception as e:
        logger.exception("Topics error")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/forecast")
async def forecast(req: ForecastRequest):
    try:
        result = forecasting_service.forecast_series(req.data)
        return MessageResponse(status="success", message="Forecast generated", data={"forecast": result})
    except Exception as e:
        logger.exception("Forecast error")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/memory/save")
async def memory_save(item: Dict[str, Any] = Body(...)):
    try:
        vector_store.save_item(item)
        return MessageResponse(status="success", message="Saved to memory")
    except Exception as e:
        logger.exception("Memory save error")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/memory/query")
async def memory_query(query: Dict[str, Any] = Body(...)):
    try:
        results = vector_store.query(query.get("q", ""))
        return MessageResponse(status="success", message="Query results", data={"results": results})
    except Exception as e:
        logger.exception("Memory query error")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze")
async def analyze_pipeline(payload: Dict[str, Any] = Body(...)):
    """Top-level orchestration endpoint that runs a LangChain-style agent flow (stubbed)."""
    try:
        res = agent_controller.run_full_analysis(payload)
        return MessageResponse(status="success", message="Analysis complete", data={"result": res})
    except Exception as e:
        logger.exception("Orchestration error")
        raise HTTPException(status_code=500, detail=str(e))
