from transformers import pipeline
import logging

logger = logging.getLogger(__name__)

classifier = pipeline(
        "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_sentiment(text: str) -> dict:
        try:
                    result = classifier(text[:512])
                            return {
                                            "label": result[0]["label"],
                                                        "score": round(result[0]["score"], 4),
                                                                    "text": text
                            }
                                except Exception as e:
                                            logger.error(f"Sentiment error: {e}")
                                                    raise e
                            }
)