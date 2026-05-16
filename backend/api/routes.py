from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from services.pandasai_service.cleaner import clean_dataset
from services.sentiment_service.analyzer import analyze_sentiment
from services.bertopic_service.topics import detect_topics
from services.forecasting_service.forecaster import forecast_data
from backend.services.gemini_service import ask_gemini
from backend.memory.vector_store import save_memory, query_memory
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


class TextInput(BaseModel):
    text: str


    class TopicsInput(BaseModel):
        documents: list[str]


        class ForecastInput(BaseModel):
            data: list[float]
                periods: int = 30


                class MemoryInput(BaseModel):
                    text: str


                    class QueryInput(BaseModel):
                        query: str


                        @router.get("/health")
                        async def health():
                            return {"status": "online"}


                            @router.post("/clean")
                            async def clean(file: UploadFile = File(...)):
                                try:
                                        result = clean_dataset(file.file)
                                                return result
                                                    except Exception as e:
                                                            logger.error(f"Clean error: {e}")
                                                                    return {"error": str(e)}


                                                                    @router.post("/sentiment")
                                                                    async def sentiment(input: TextInput):
                                                                        try:
                                                                                result = analyze_sentiment(input.text)
                                                                                        return {"result": result}
                                                                                            except Exception as e:
                                                                                                    logger.error(f"Sentiment error: {e}")
                                                                                                            return {"error": str(e)}


                                                                                                            @router.post("/topics")
                                                                                                            async def topics(input: TopicsInput):
                                                                                                                try:
                                                                                                                        result = detect_topics(input.documents)
                                                                                                                                return result
                                                                                                                                    except Exception as e:
                                                                                                                                            logger.error(f"Topics error: {e}")
                                                                                                                                                    return {"error": str(e)}


                                                                                                                                                    @router.post("/forecast")
                                                                                                                                                    async def forecast(input: ForecastInput):
                                                                                                                                                        try:
                                                                                                                                                                result = forecast_data(input.data, input.periods)
                                                                                                                                                                        return result
                                                                                                                                                                            except Exception as e:
                                                                                                                                                                                    logger.error(f"Forecast error: {e}")
                                                                                                                                                                                            return {"error": str(e)}


                                                                                                                                                                                            @router.post("/analyze")
                                                                                                                                                                                            async def analyze(input: TextInput):
                                                                                                                                                                                                try:
                                                                                                                                                                                                        result = await ask_gemini(input.text)
                                                                                                                                                                                                                return {"result": result}
                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                            logger.error(f"Analyze error: {e}")
                                                                                                                                                                                                                                    return {"error": str(e)}


                                                                                                                                                                                                                                    @router.post("/memory/save")
                                                                                                                                                                                                                                    async def memory_save(input: MemoryInput):
                                                                                                                                                                                                                                        try:
                                                                                                                                                                                                                                                save_memory(input.text)
                                                                                                                                                                                                                                                        return {"status": "saved"}
                                                                                                                                                                                                                                                            except Exception as e:
                                                                                                                                                                                                                                                                    logger.error(f"Memory save error: {e}")
                                                                                                                                                                                                                                                                            return {"error": str(e)}


                                                                                                                                                                                                                                                                            @router.post("/memory/query")
                                                                                                                                                                                                                                                                            async def memory_query(input: QueryInput):
                                                                                                                                                                                                                                                                                try:
                                                                                                                                                                                                                                                                                        result = query_memory(input.query)
                                                                                                                                                                                                                                                                                                return {"result": result}
                                                                                                                                                                                                                                                                                                    except Exception as e:
                                                                                                                                                                                                                                                                                                            logger.error(f"Memory query error: {e}")
                                                                                                                                                                                                                                                                                                                    return {"error": str(e)}