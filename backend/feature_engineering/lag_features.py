import pandas as pd


def add_lag_features(data):

    print("\n========== ADDING LAG & ROLLING FEATURES ==========\n")

    # =====================================================
    # SORT DATA
    # =====================================================

    data = (
        data
        .sort_values(["company_id", "trade_date"])
        .reset_index(drop=True)
    )

    # =====================================================
    # CLOSE PRICE LAGS
    # =====================================================

    data["close_lag_1"] = data.groupby("company_id")["close"].shift(1)
    data["close_lag_2"] = data.groupby("company_id")["close"].shift(2)
    data["close_lag_3"] = data.groupby("company_id")["close"].shift(3)
    data["close_lag_5"] = data.groupby("company_id")["close"].shift(5)
    data["close_lag_10"] = data.groupby("company_id")["close"].shift(10)

    # =====================================================
    # VOLUME LAGS
    # =====================================================

    data["volume_lag_1"] = data.groupby("company_id")["volume"].shift(1)
    data["volume_lag_5"] = data.groupby("company_id")["volume"].shift(5)

    # =====================================================
    # OPEN, HIGH & LOW LAGS
    # =====================================================

    data["open_lag_1"] = data.groupby("company_id")["open"].shift(1)
    data["high_lag_1"] = data.groupby("company_id")["high"].shift(1)
    data["low_lag_1"] = data.groupby("company_id")["low"].shift(1)

    # =====================================================
    # ROLLING FEATURES (20 DAYS)
    # =====================================================

    data["rolling_mean_20"] = (
        data.groupby("company_id")["close"]
        .rolling(window=20)
        .mean()
        .reset_index(level=0, drop=True)
    )

    data["rolling_max_20"] = (
        data.groupby("company_id")["close"]
        .rolling(window=20)
        .max()
        .reset_index(level=0, drop=True)
    )

    data["rolling_min_20"] = (
        data.groupby("company_id")["close"]
        .rolling(window=20)
        .min()
        .reset_index(level=0, drop=True)
    )

    data["rolling_std_20"] = (
        data.groupby("company_id")["close"]
        .rolling(window=20)
        .std()
        .reset_index(level=0, drop=True)
    )

    data["rolling_median_20"] = (
        data.groupby("company_id")["close"]
        .rolling(window=20)
        .median()
        .reset_index(level=0, drop=True)
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
                "close_lag_1",
                "close_lag_5",
                "volume_lag_1",
                "rolling_mean_20",
                "rolling_max_20",
                "rolling_min_20",
                "rolling_std_20",
                "rolling_median_20"
            ]
        ].tail(30)
    )

    print("\nLag & Rolling Features Created!\n")

    return data