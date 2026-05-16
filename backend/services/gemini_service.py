"""Gemini service stub.
This module provides a small wrapper around the Google Generative AI (Gemini) client.
For now it returns mocked responses. Replace with real API calls and authentication.
"""
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


def generate_insight(prompt: str) -> Dict[str, Any]:
    """Generate an insight from Gemini. Replace with real client call."""
    logger.info("generate_insight called")
    # TODO: integrate google-generativeai client
    return {"prompt": prompt, "insight": "This is a mocked insight from Gemini."}
