"""Agent controller stub to orchestrate simple flows.
Replace with LangChain agents and tools for production workloads.
"""
from typing import Any, Dict, List
import logging

from backend.services import gemini_service
from services.pandasai_service import cleaner as pandasai_cleaner
from services.sentiment_service import analyzer as sentiment_analyzer
from services.bertopic_service import topics as bertopic_service
from services.forecasting_service import forecaster as forecasting_service

logger = logging.getLogger(__name__)


def list_agents() -> List[str]:
    return ["cleaning", "sentiment", "trend", "forecast", "report", "research"]


def run_full_analysis(payload: Dict[str, Any]) -> Dict[str, Any]:
    # Minimal orchestrator: run available steps if present in payload
    result: Dict[str, Any] = {}
    if payload.get("data_csv_bytes"):
        result["clean"] = pandasai_cleaner.clean_csv_bytes(payload["data_csv_bytes"])
    if payload.get("text"):
        result["sentiment"] = sentiment_analyzer.analyze_text(payload["text"])
    if payload.get("documents"):
        result["topics"] = bertopic_service.detect_topics(payload["documents"])
    if payload.get("series"):
        result["forecast"] = forecasting_service.forecast_series(payload["series"])

    # Generate a short summary via Gemini (mocked)
    result["insight"] = gemini_service.generate_insight("Summarize results")
    logger.info("run_full_analysis completed")
    return result
