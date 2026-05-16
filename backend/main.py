from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Marketing Intelligence Platform",
        description="Autonomous AI marketing analysis platform",
            version="1.0.0"
            )

            app.add_middleware(
                CORSMiddleware,
                    allow_origins=["*"],
                        allow_credentials=True,
                            allow_methods=["*"],
                                allow_headers=["*"],
                                )

                                app.include_router(router)

                                @app.get("/health")
                                async def health():
                                    return {"status": "online", "message": "AI Marketing Platform running"}