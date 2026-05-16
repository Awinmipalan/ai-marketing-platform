"""Forecasting service stub using Prophet (mocked).
Replace with real Prophet model training and forecasting.
"""
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


def forecast_series(data: List[float]) -> Dict[str, Any]:
    logger.info("forecast_series called with %d points", len(data))
    # Simple linear extrapolation for demo purposes
    if not data:
        return {"error": "no data"}
    last = data[-1]
    forecast = [last * (1 + 0.01 * i) for i in range(1, 8)]
    return {"forecast": forecast, "method": "mock_linear"}
