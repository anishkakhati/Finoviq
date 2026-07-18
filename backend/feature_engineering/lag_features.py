import pandas as pd


def add_lag_features(data):

    print("\n========== ADDING LAG & ROLLING FEATURES ==========\n")

    # =====================================================
    # CLOSE PRICE LAGS
    # =====================================================

    data["close_lag_1"] = data["close"].shift(1)
    data["close_lag_2"] = data["close"].shift(2)
    data["close_lag_3"] = data["close"].shift(3)
    data["close_lag_5"] = data["close"].shift(5)
    data["close_lag_10"] = data["close"].shift(10)

    # =====================================================
    # VOLUME LAGS
    # =====================================================

    data["volume_lag_1"] = data["volume"].shift(1)
    data["volume_lag_5"] = data["volume"].shift(5)

    # =====================================================
    # OPEN, HIGH & LOW LAGS
    # =====================================================

    data["open_lag_1"] = data["open"].shift(1)
    data["high_lag_1"] = data["high"].shift(1)
    data["low_lag_1"] = data["low"].shift(1)

    # =====================================================
    # ROLLING FEATURES (20 DAYS)
    # =====================================================

    # Rolling Mean
    data["rolling_mean_20"] = data["close"].rolling(window=20).mean()

    # Rolling Maximum
    data["rolling_max_20"] = data["close"].rolling(window=20).max()

    # Rolling Minimum
    data["rolling_min_20"] = data["close"].rolling(window=20).min()

    # Rolling Standard Deviation
    data["rolling_std_20"] = data["close"].rolling(window=20).std()

    # Rolling Median
    data["rolling_median_20"] = data["close"].rolling(window=20).median()

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    print(
        data[
            [
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