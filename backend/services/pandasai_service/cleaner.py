import logging
import pandas as pd

logger = logging.getLogger(__name__)


def clean_dataset(file) -> dict:
    try:
        df = pd.read_csv(file)
        missing = df.isnull().sum().to_dict()

        before = len(df)
        df = df.drop_duplicates()
        after = len(df)
        duplicates_removed = before - after

        for col in df.select_dtypes(include="number").columns:
            df[col].fillna(df[col].mean(), inplace=True)
        for col in df.select_dtypes(include="object").columns:
            df[col].fillna("unknown", inplace=True)

        return {
            "status": "cleaned",
            "rows": len(df),
            "columns": df.columns.tolist(),
            "duplicates_removed": duplicates_removed,
            "missing_values": missing,
        }
    except Exception as e:
        logger.error(f"Cleaning error: {e}")
        raise e
