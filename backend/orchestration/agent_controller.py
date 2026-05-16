import logging

from backend.services.gemini_service import ask_gemini

logger = logging.getLogger(__name__)


async def run_cleaning_agent(prompt: str) -> str:
    try:
        result = await ask_gemini(f"You are a data cleaning expert. {prompt}")
        return result
    except Exception as e:
        logger.error(f"Cleaning agent error: {e}")
        raise e


async def run_sentiment_agent(prompt: str) -> str:
    try:
        result = await ask_gemini(f"You are a sentiment analysis expert. {prompt}")
        return result
    except Exception as e:
        logger.error(f"Sentiment agent error: {e}")
        raise e


async def run_trend_agent(prompt: str) -> str:
    try:
        result = await ask_gemini(f"You are a market trend expert. {prompt}")
        return result
    except Exception as e:
        logger.error(f"Trend agent error: {e}")
        raise e


async def run_forecast_agent(prompt: str) -> str:
    try:
        result = await ask_gemini(f"You are a forecasting expert. {prompt}")
        return result
    except Exception as e:
        logger.error(f"Forecast agent error: {e}")
        raise e


async def run_report_agent(prompt: str) -> str:
    try:
        result = await ask_gemini(f"You are an executive report writer. {prompt}")
        return result
    except Exception as e:
        logger.error(f"Report agent error: {e}")
        raise e


async def run_research_agent(prompt: str) -> str:
    try:
        result = await ask_gemini(f"You are a market research expert. {prompt}")
        return result
    except Exception as e:
        logger.error(f"Research agent error: {e}")
        raise e
