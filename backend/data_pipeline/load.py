import pandas as pd
import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


# ==========================================================
# Helper Functions
# ==========================================================

def safe_float(value):
    """Convert value to float or None if NaN."""
    if pd.isna(value):
        return None
    return float(value)


def safe_int(value):
    """Convert value to int or None if NaN."""
    if pd.isna(value):
        return None
    return int(value)


# ==========================================================
# Load Data into PostgreSQL
# ==========================================================

def load_data(data):

    print("\n========== LOADING PROCESSED DATA ==========\n")

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO processed_stock_data
    (
        company_id,
        trade_date,

        open,
        high,
        low,
        close,
        volume,

        daily_return,
        price_range,
        candle_size,
        volatility,

        sma_20,
        ema_12,
        ema_26,

        rsi_14,

        macd,
        macd_signal,
        macd_histogram,

        bb_upper,
        bb_middle,
        bb_lower,

        atr_14,

        obv,

        vwap,

        close_lag_1,
        close_lag_2,
        close_lag_3,
        close_lag_5,
        close_lag_10,

        volume_lag_1,
        volume_lag_5,

        open_lag_1,
        high_lag_1,
        low_lag_1,

        rolling_mean_20,
        rolling_std_20,
        rolling_max_20,
        rolling_min_20,
        rolling_median_20
    )

    VALUES
    (
        %s,%s,

        %s,%s,%s,%s,%s,%s,

        %s,%s,%s,%s,

        %s,%s,%s,

        %s,

        %s,%s,%s,

        %s,%s,%s,

        %s,

        %s,

        %s,

        %s,%s,%s,%s,%s,

        %s,%s,

        %s,%s,%s,

        %s,%s,%s,%s,%s
    )

    ON CONFLICT (company_id, trade_date)
    DO NOTHING;
    """

    inserted_rows = 0

    for _, row in data.iterrows():

        try:

            cursor.execute(
                insert_query,
                (
                    # Basic Information
                    safe_int(row["company_id"]),
                    row["trade_date"].date(),

                    # OHLCV
                    safe_float(row["open"]),
                    safe_float(row["high"]),
                    safe_float(row["low"]),
                    safe_float(row["close"]),
                    safe_int(row["volume"]),

                    # Basic Features
                    safe_float(row["daily_return"]),
                    safe_float(row["price_range"]),
                    safe_float(row["candle_size"]),
                    safe_float(row["volatility"]),

                    # Moving Averages
                    safe_float(row["SMA_20"]),
                    safe_float(row["EMA_12"]),
                    safe_float(row["EMA_26"]),

                    # RSI
                    safe_float(row["RSI_14"]),

                    # MACD
                    safe_float(row["MACD"]),
                    safe_float(row["MACD_Signal"]),
                    safe_float(row["MACD_Histogram"]),

                    # Bollinger Bands
                    safe_float(row["BB_Upper"]),
                    safe_float(row["BB_Middle"]),
                    safe_float(row["BB_Lower"]),

                    # ATR
                    safe_float(row["ATR_14"]),

                    # OBV
                    safe_int(row["OBV"]),

                    # VWAP
                    safe_float(row["VWAP"]),

                    # Lag Features
                    safe_float(row["close_lag_1"]),
                    safe_float(row["close_lag_2"]),
                    safe_float(row["close_lag_3"]),
                    safe_float(row["close_lag_5"]),
                    safe_float(row["close_lag_10"]),

                    safe_int(row["volume_lag_1"]),
                    safe_int(row["volume_lag_5"]),

                    safe_float(row["open_lag_1"]),
                    safe_float(row["high_lag_1"]),
                    safe_float(row["low_lag_1"]),

                    # Rolling Features
                    safe_float(row["rolling_mean_20"]),
                    safe_float(row["rolling_std_20"]),
                    safe_float(row["rolling_max_20"]),
                    safe_float(row["rolling_min_20"]),
                    safe_float(row["rolling_median_20"])
                )
            )

            inserted_rows += 1

        except Exception as e:

            print("\n=========== ROW THAT FAILED ===========")

            for key, value in row.items():
                print(f"{key:25}: {value}")

            print("\nERROR:", e)

            connection.rollback()

            raise

    connection.commit()

    cursor.close()
    connection.close()

    print(f"\nSuccessfully inserted {inserted_rows} rows.")
    print("Processed Data Loaded Successfully!")