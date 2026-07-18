import pandas as pd


def add_indicators(data):

    print("\n========== ADDING TECHNICAL INDICATORS ==========\n")

    # -----------------------------
    # Simple Moving Averages (SMA)
    # -----------------------------
    data["SMA_5"] = data["close"].rolling(window=5).mean()
    data["SMA_10"] = data["close"].rolling(window=10).mean()
    data["SMA_20"] = data["close"].rolling(window=20).mean()
    data["SMA_50"] = data["close"].rolling(window=50).mean()
    data["SMA_200"] = data["close"].rolling(window=200).mean()

    # -----------------------------
    # Exponential Moving Averages
    # -----------------------------

    data["EMA_12"] = data["close"].ewm(span=12, adjust=False).mean()
    data["EMA_26"] = data["close"].ewm(span=26, adjust=False).mean()

    # -----------------------------
    # RSI (14)
    # -----------------------------

    delta = data["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    data["RSI_14"] = 100 - (100 / (1 + rs))

    # -----------------------------
    # MACD
    # -----------------------------

    data["MACD"] = data["EMA_12"] - data["EMA_26"]
    data["MACD_Signal"] = (data["MACD"].ewm(span=9, adjust=False).mean())
    data["MACD_Histogram"] = (data["MACD"] - data["MACD_Signal"])

    # -----------------------------
    # Bollinger Bands
    # -----------------------------

    rolling_std = data["close"].rolling(window=20).std()
    data["BB_Upper"] = data["SMA_20"] + (2 * rolling_std)
    data["BB_Middle"] = data["SMA_20"]
    data["BB_Lower"] = data["SMA_20"] - (2 * rolling_std)

    # -----------------------------
    # ATR (Average True Range)
    # -----------------------------

    # Previous day's closing price
    previous_close = data["close"].shift(1)
    high_low = data["high"] - data["low"]
    high_close = (data["high"] - previous_close).abs()
    low_close = (data["low"] - previous_close).abs()
    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)
    data["ATR_14"] = true_range.rolling(window=14).mean()

    # -----------------------------
    # OBV (On Balance Volume)
    # -----------------------------

    obv = [0]

    for i in range(1, len(data)):

        if data["close"].iloc[i] > data["close"].iloc[i - 1]:
            obv.append(obv[-1] + data["volume"].iloc[i])

        elif data["close"].iloc[i] < data["close"].iloc[i - 1]:
            obv.append(obv[-1] - data["volume"].iloc[i])

        else:
            obv.append(obv[-1])

    data["OBV"] = obv

    # -----------------------------
    # VWAP (Volume Weighted Average Price)
    # -----------------------------

    typical_price = (
        data["high"] +
        data["low"] +
        data["close"]
    ) / 3

    data["VWAP"] = (
        (typical_price * data["volume"]).cumsum()
        / data["volume"].cumsum()
    )

    print(
    data[
        [
            "trade_date",
            "close",
            "volume",
            "VWAP"
        ]
    ].head(30)
    )
    return data