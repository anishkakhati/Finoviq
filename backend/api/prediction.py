from fastapi import FastAPI
from pydantic import BaseModel

from backend.models.predict import predict_next_day

app = FastAPI()


class StockInput(BaseModel):

    company_id: int

    open: float

    high: float

    low: float

    close: float

    volume: int

    daily_return: float

    price_range: float

    candle_size: float

    volatility: float

    sma_20: float

    ema_12: float

    ema_26: float

    rsi_14: float

    macd: float

    macd_signal: float

    macd_histogram: float

    bb_upper: float

    bb_middle: float

    bb_lower: float

    atr_14: float

    obv: int

    vwap: float

    close_lag_1: float

    close_lag_2: float

    close_lag_3: float

    close_lag_5: float

    close_lag_10: float

    volume_lag_1: float

    volume_lag_5: float

    open_lag_1: float

    high_lag_1: float

    low_lag_1: float

    rolling_std_20: float

    rolling_max_20: float

    rolling_min_20: float

    rolling_median_20: float


@app.post("/predict")

def predict(stock: StockInput):

    prediction = predict_next_day(
        stock.model_dump()
    )

    return {

        "Predicted Close Price": prediction

    }