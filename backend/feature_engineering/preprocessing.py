import pandas as pd


def preprocess_data(data):

    print("\n========== PREPROCESSING DATA ==========\n")

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Fill missing values
    data = data.ffill()

    # Ensure trade_date is datetime
    data["trade_date"] = pd.to_datetime(data["trade_date"])

    # Sort by date
    data = data.sort_values("trade_date")

    # Reset index
    data = data.reset_index(drop=True)

    # Daily Return
    data["daily_return"] = data["close"].pct_change()

    # Price Range
    data["price_range"] = data["high"] - data["low"]

    # Candle Size
    data["candle_size"] = data["close"] - data["open"]

    # Volatility (20-day rolling standard deviation)
    data["volatility"] = data["daily_return"].rolling(window=20).std()

    print(data.head(25))

    print("\n Preprocessing Complete!\n")

    return data