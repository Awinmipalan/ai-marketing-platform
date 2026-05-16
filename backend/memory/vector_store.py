"""Simple in-repo vector store stub for ChromaDB.
Replace with chromadb client integration for production.
"""
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

# In-memory store for demo
_STORE: List[Dict[str, Any]] = []


def save_item(item: Dict[str, Any]) -> None:
    _STORE.append(item)
    logger.info("Item saved to in-memory vector store. Total=%d", len(_STORE))


def query(q: str) -> List[Dict[str, Any]]:
    # Very naive search
    results = [it for it in _STORE if q.lower() in str(it).lower()]
    logger.info("Query for '%s' returned %d results", q, len(results))
    return results
