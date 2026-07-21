import pandas as pd


def add_indicators(data):

    print("\n========== ADDING TECHNICAL INDICATORS ==========\n")

    # =====================================================
    # Sort by company and date
    # =====================================================

    data = (
        data
        .sort_values(["company_id", "trade_date"])
        .reset_index(drop=True)
    )

    # =====================================================
    # SIMPLE MOVING AVERAGES
    # =====================================================

    for window in [5, 10, 20, 50, 200]:

        data[f"SMA_{window}"] = (
            data.groupby("company_id")["close"]
            .rolling(window)
            .mean()
            .reset_index(level=0, drop=True)
        )

    # =====================================================
    # EXPONENTIAL MOVING AVERAGES
    # =====================================================

    data["EMA_12"] = (
        data.groupby("company_id")["close"]
        .transform(lambda x: x.ewm(span=12, adjust=False).mean())
    )

    data["EMA_26"] = (
        data.groupby("company_id")["close"]
        .transform(lambda x: x.ewm(span=26, adjust=False).mean())
    )

    # =====================================================
    # RSI (14)
    # =====================================================

    delta = data.groupby("company_id")["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = (
        gain.groupby(data["company_id"])
        .rolling(14)
        .mean()
        .reset_index(level=0, drop=True)
    )

    avg_loss = (
        loss.groupby(data["company_id"])
        .rolling(14)
        .mean()
        .reset_index(level=0, drop=True)
    )

    rs = avg_gain / avg_loss

    data["RSI_14"] = 100 - (100 / (1 + rs))

    # =====================================================
    # MACD
    # =====================================================

    data["MACD"] = data["EMA_12"] - data["EMA_26"]

    data["MACD_Signal"] = (
        data.groupby("company_id")["MACD"]
        .transform(lambda x: x.ewm(span=9, adjust=False).mean())
    )

    data["MACD_Histogram"] = (
        data["MACD"] - data["MACD_Signal"]
    )

    # =====================================================
    # BOLLINGER BANDS
    # =====================================================

    rolling_std = (
        data.groupby("company_id")["close"]
        .rolling(20)
        .std()
        .reset_index(level=0, drop=True)
    )

    data["BB_Upper"] = data["SMA_20"] + (2 * rolling_std)
    data["BB_Middle"] = data["SMA_20"]
    data["BB_Lower"] = data["SMA_20"] - (2 * rolling_std)

    # =====================================================
    # ATR (14)
    # =====================================================

    previous_close = (
        data.groupby("company_id")["close"]
        .shift(1)
    )

    high_low = data["high"] - data["low"]
    high_close = (data["high"] - previous_close).abs()
    low_close = (data["low"] - previous_close).abs()

    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    data["ATR_14"] = (
        true_range
        .groupby(data["company_id"])
        .rolling(14)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # =====================================================
    # OBV
    # =====================================================

    data["OBV"] = 0

    for company in data["company_id"].unique():

        company_index = data[data["company_id"] == company].index

        obv = [0]

        for i in range(1, len(company_index)):

            current = company_index[i]
            previous = company_index[i - 1]

            if data.loc[current, "close"] > data.loc[previous, "close"]:
                obv.append(obv[-1] + data.loc[current, "volume"])

            elif data.loc[current, "close"] < data.loc[previous, "close"]:
                obv.append(obv[-1] - data.loc[current, "volume"])

            else:
                obv.append(obv[-1])

        data.loc[company_index, "OBV"] = obv

    # =====================================================
    # VWAP
    # =====================================================

    typical_price = (
        data["high"] +
        data["low"] +
        data["close"]
    ) / 3

    tpv = typical_price * data["volume"]

    data["VWAP"] = (
        tpv.groupby(data["company_id"]).cumsum()
        /
        data["volume"].groupby(data["company_id"]).cumsum()
    )

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    print(
        data[
            [
                "company_id",
                "trade_date",
                "close",
                "VWAP"
            ]
        ].head(30)
    )

    print("\n========== BOLLINGER BAND CHECK ==========\n")

    print(
        data[
            [
                "company_id",
                "SMA_20",
                "BB_Upper",
                "BB_Middle",
                "BB_Lower"
            ]
        ].tail(20)
    )

    print("\nTechnical Indicators Created Successfully!\n")

    return data