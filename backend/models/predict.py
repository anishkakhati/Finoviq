import joblib
import pandas as pd

from datetime import date

from backend.database.save_prediction import save_prediction

# ==========================================================
# LOAD BEST MODEL
# ==========================================================

model = joblib.load(
    "backend/saved_models/best_model.pkl"
)

# ==========================================================
# LOAD SCALER
# ==========================================================

scaler = joblib.load(
    "backend/saved_models/scaler.pkl"
)

# ==========================================================
# LOAD FEATURE ORDER
# ==========================================================

feature_columns = joblib.load(
    "backend/saved_models/feature_columns.pkl"
)


def predict_next_day(stock_data):

    print("\n========== INPUT DATA ==========\n")

    data = pd.DataFrame([stock_data])

    print(data)

    # ==========================================================
    # REORDER FEATURES
    # ==========================================================

    data = data[feature_columns]

    print("\n========== REORDERED FEATURES ==========\n")

    print(data)

    # ==========================================================
    # SCALE INPUT
    # ==========================================================

    data = scaler.transform(data)

    # ==========================================================
    # PREDICT
    # ==========================================================

    prediction = model.predict(data)[0]

    result = {

        "open": round(float(prediction[0]), 2),

        "high": round(float(prediction[1]), 2),

        "low": round(float(prediction[2]), 2),

        "close": round(float(prediction[3]), 2)

    }

    # ==========================================================
    # SAVE PREDICTION TO DATABASE
    # ==========================================================

    save_prediction(

        company_id=stock_data["company_id"],

        prediction_date=date.today(),

        predicted_open=result["open"],

        predicted_high=result["high"],

        predicted_low=result["low"],

        predicted_close=result["close"],

        confidence=0.95,

        model_version="Multi-Output Linear Regression"

    )

    # ==========================================================
    # DISPLAY RESULTS
    # ==========================================================

    print("\n========== TOMORROW MARKET FORECAST ==========\n")

    print(f"Open  : {result['open']}")
    print(f"High  : {result['high']}")
    print(f"Low   : {result['low']}")
    print(f"Close : {result['close']}")

    return result


if __name__ == "__main__":

    sample_input = {

        "company_id": 1,

        "open": 229.0,

        "high": 231.0,

        "low": 228.0,

        "close": 230.0,

        "volume": 52000000,

        "daily_return": 0.01,

        "price_range": 3.0,

        "candle_size": 1.0,

        "volatility": 0.02,

        "sma_20": 226.0,

        "rsi_14": 58.0,

        "macd": 1.50,

        "atr_14": 2.30,

        "obv": 120000000,

        "vwap": 229.0,

        "close_lag_1": 229.0,

        "close_lag_2": 228.0,

        "close_lag_3": 227.0,

        "volume_lag_1": 51000000,

        "rolling_std_20": 2.50

    }

    prediction = predict_next_day(sample_input)

    print("\nPrediction Dictionary:\n")

    print(prediction)