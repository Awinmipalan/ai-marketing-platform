"""BERTopic service stub.
Methods return mocked topics to be replaced with real BERTopic calls.
"""
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


def detect_topics(documents: List[str]) -> List[Dict[str, Any]]:
    logger.info("detect_topics called with %d documents", len(documents))
    # TODO: Integrate BERTopic; return a mocked list
    return [{"topic": "marketing_trend", "score": 0.87, "representative_docs": documents[:3]}]
