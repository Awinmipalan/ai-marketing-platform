"""PandasAI cleaner stub.
Accepts CSV bytes and returns a small cleaning summary.
"""
from typing import Dict, Any
import pandas as pd
import io
import logging

logger = logging.getLogger(__name__)


def clean_csv_bytes(contents: bytes) -> Dict[str, Any]:
    """Read CSV bytes, perform lightweight cleaning, and return a summary."""
    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception:
        # Try decode as utf-8 text
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))

    before = len(df)
    # Simple cleaning steps
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    after = len(df)

    summary = {
        "rows_before": before,
        "rows_after": after,
        "columns": list(df.columns),
    }
    logger.info("clean_csv_bytes summary: %s", summary)
    return summary
