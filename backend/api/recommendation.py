from fastapi import APIRouter

from backend.schemas.stock import StockInput

from backend.models.predict import predict_next_day

from backend.trading.strategy import generate_trade_strategy

from backend.database.save_recommendation import save_recommendation


router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)


@router.post("/recommend")
def recommend(stock: StockInput):

    # ==========================================================
    # STEP 1 : Predict Tomorrow
    # ==========================================================

    prediction = predict_next_day(stock.model_dump())

    # ==========================================================
    # STEP 2 : Convert Numeric Volatility
    # ==========================================================

    if stock.volatility < 0.015:
        volatility = "low"

    elif stock.volatility < 0.03:
        volatility = "medium"

    else:
        volatility = "high"

    # ==========================================================
    # STEP 3 : Estimate Trend Strength
    # ==========================================================

    if prediction["close"] > stock.close:

        trend_strength = 1 + (
            (prediction["close"] - stock.close)
            / stock.close
        )

    else:

        trend_strength = 0.95

    # ==========================================================
    # STEP 4 : Trading Strategy Engine
    # ==========================================================

    recommendation = generate_trade_strategy(

        predicted_open=prediction["open"],

        predicted_high=prediction["high"],

        predicted_low=prediction["low"],

        predicted_close=prediction["close"],

        current_close=stock.close,

        rsi=stock.rsi_14,

        macd=stock.macd,

        atr=stock.atr_14,

        trend_strength=trend_strength,

        volatility=volatility,

        investment=stock.investment,

    )

    # ==========================================================
    # STEP 5 : Save Recommendation
    # ==========================================================

    save_recommendation(

        company_id=stock.company_id,

        recommendation=recommendation["recommendation"]["recommendation"],

        entry_price=recommendation["entry"]["entry_price"],

        exit_price=recommendation["exit"]["exit_price"],

        stop_loss=recommendation["stop_loss"]["stop_loss"],

        take_profit=recommendation["take_profit"]["take_profit"],

        expected_profit=recommendation["profit"]["expected_profit"],

        expected_loss=recommendation["profit"]["expected_loss"],

        roi=recommendation["profit"]["roi"],

        confidence=recommendation["confidence"]["confidence"]

    )

    # ==========================================================
    # STEP 6 : Return Response
    # ==========================================================

    return {

        "status": "success",

        "company_id": stock.company_id,

        "prediction": prediction,

        "recommendation": recommendation

    }