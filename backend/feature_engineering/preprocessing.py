import pandas as pd


def preprocess_data(data):

    print("\n========== PREPROCESSING DATA ==========\n")

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Ensure trade_date is datetime
    data["trade_date"] = pd.to_datetime(data["trade_date"])

    # Sort by company and date
    data = (
        data
        .sort_values(["company_id", "trade_date"])
        .reset_index(drop=True)
    )

    # Daily Return
    data["daily_return"] = (
        data.groupby("company_id")["close"]
        .pct_change()
    )

    # Price Range
    data["price_range"] = data["high"] - data["low"]

    # Candle Size
    data["candle_size"] = data["close"] - data["open"]

    # Volatility
    data["volatility"] = (
        data.groupby("company_id")["daily_return"]
        .rolling(window=20)
        .std()
        .reset_index(level=0, drop=True)
    )

    print(data.head(25))

    print("\nPreprocessing Complete!\n")

    return data