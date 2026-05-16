import logging
from datetime import datetime, timedelta

import pandas as pd

logger = logging.getLogger(__name__)


def forecast_data(data: list[float], periods: int = 30) -> dict:
    try:
        dates = [datetime.today() - timedelta(days=len(data) - i) for i in range(len(data))]
        df = pd.DataFrame({"ds": dates, "y": data})

        try:
            from prophet import Prophet

            model = Prophet()
            model.fit(df)
            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)

            return {
                "status": "success",
                "method": "prophet",
                "forecast": forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
                .tail(periods)
                .to_dict(orient="records"),
            }
        except Exception:
            avg = sum(data[-7:]) / min(7, len(data))
            forecast = [avg] * periods
            return {
                "status": "success",
                "method": "moving_average",
                "forecast": forecast,
            }
    except Exception as e:
        logger.error(f"Forecast error: {e}")
        raise e
