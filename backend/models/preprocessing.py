import pandas as pd
import psycopg2
import joblib

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def load_dataset(model_type="linear"):
    """
    Load processed stock data from PostgreSQL
    and prepare it for Machine Learning.

    model_type:
        "linear" -> Selected features for Linear Regression
        "tree"   -> All engineered features for Random Forest/XGBoost
    """

    print("\n========== LOADING DATASET FROM POSTGRESQL ==========\n")

    # ==========================================================
    # CONNECT TO DATABASE
    # ==========================================================

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    print("Connected to PostgreSQL Successfully!")

    query = """
    SELECT *
    FROM processed_stock_data
    ORDER BY company_id, trade_date;
    """

    data = pd.read_sql_query(query, connection)

    connection.close()

    print("\nDataset Loaded Successfully!\n")

    print("Shape of Dataset:")
    print(data.shape)

    print("\nColumn Names:")
    print(data.columns)

    print("\nFirst 5 Rows:")
    print(data.head())

    # ==========================================================
    # STEP 1 : CREATE TARGET VARIABLE
    # ==========================================================

    print("\n========== CREATING TARGET VARIABLE ==========\n")

    data["target_close"] = (
        data.groupby("company_id")["close"]
        .shift(-1)
    )

    print(
        data[
            [
                "company_id",
                "trade_date",
                "close",
                "target_close"
            ]
        ].head(10)
    )

    # ==========================================================
    # STEP 2 : CLEAN DATASET
    # ==========================================================

    print("\n========== CLEANING DATASET ==========\n")

    data = data.drop(
        columns=[
            "id",
            "trade_date",
            "created_at"
        ]
    )

    data = data.dropna(subset=["target_close"])

    data = data.dropna()

    print("\nMissing Values After Cleaning:\n")
    print(data.isnull().sum())

    print("\nDataset Shape After Cleaning:")
    print(data.shape)

    # Remove one redundant feature for all models
    data = data.drop(columns=["rolling_mean_20"])

    # ==========================================================
    # FEATURE SELECTION
    # ==========================================================

    if model_type == "linear":

        print("\n========== SELECTING FEATURES FOR LINEAR REGRESSION ==========\n")

        selected_features = [

            "company_id",

            "open",
            "high",
            "low",
            "close",

            "volume",

            "daily_return",

            "price_range",
            "candle_size",

            "volatility",

            "sma_20",

            "rsi_14",

            "macd",

            "atr_14",

            "obv",

            "vwap",

            "close_lag_1",
            "close_lag_2",
            "close_lag_3",

            "volume_lag_1",

            "rolling_std_20"

        ]

        X = data[selected_features]

    elif model_type == "tree":

        print("\n========== USING ALL FEATURES FOR TREE MODELS ==========\n")

        X = data.drop(columns=["target_close"])

    else:

        raise ValueError(
            "model_type must be either 'linear' or 'tree'"
        )

    # ==========================================================
    # TARGET
    # ==========================================================

    y = data["target_close"]

    print("Features Shape:", X.shape)
    print("Target Shape:", y.shape)

    print("\nFeature Columns:")
    print(X.columns)

    # ==========================================================
    # SAVE FEATURE ORDER
    # ==========================================================

    joblib.dump(
        list(X.columns),
        "backend/saved_models/feature_columns.pkl"
    )

    print("\nFeature columns saved successfully!")

    print("\nFirst 5 Target Values:")
    print(y.head())

    return X, y, data


if __name__ == "__main__":

    X, y, data = load_dataset(model_type="linear")