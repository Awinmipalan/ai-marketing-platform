"""Sentiment analyzer stub using transformers (mocked).
Replace with real HuggingFace pipeline calls for production.
"""
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


def analyze_text(text: str) -> Dict[str, Any]:
    logger.info("analyze_text called")
    # TODO: Use transformers pipeline('sentiment-analysis')
    score = 0.1 if "bad" in text.lower() else 0.9
    label = "NEGATIVE" if score < 0.5 else "POSITIVE"
    return {"label": label, "score": score}
