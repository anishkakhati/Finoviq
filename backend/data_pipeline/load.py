import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


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
        adj_close,
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
        %s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,
        %s,%s,%s,
        %s,
        %s,%s,%s,
        %s,%s,
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
                    int(row["company_id"]),
                    row["trade_date"].date(),

                    float(row["open"]),
                    float(row["high"]),
                    float(row["low"]),
                    float(row["close"]),
                    float(row["adj_close"]),
                    int(row["volume"]),

                    float(row["daily_return"]),
                    float(row["price_range"]),
                    float(row["candle_size"]),
                    float(row["volatility"]),

                    float(row["SMA_20"]),
                    float(row["EMA_12"]),
                    float(row["EMA_26"]),

                    float(row["RSI_14"]),

                    float(row["MACD"]),
                    float(row["MACD_Signal"]),
                    float(row["MACD_Histogram"]),

                    float(row["BB_Upper"]),
                    float(row["BB_Lower"]),

                    float(row["ATR_14"]),

                    int(row["OBV"]),

                    float(row["VWAP"]),

                    float(row["close_lag_1"]) if not psycopg2.extensions.AsIs(str(row["close_lag_1"])) else None,
                    float(row["close_lag_2"]) if not psycopg2.extensions.AsIs(str(row["close_lag_2"])) else None,
                    float(row["close_lag_3"]) if not psycopg2.extensions.AsIs(str(row["close_lag_3"])) else None,
                    float(row["close_lag_5"]) if not psycopg2.extensions.AsIs(str(row["close_lag_5"])) else None,
                    float(row["close_lag_10"]) if not psycopg2.extensions.AsIs(str(row["close_lag_10"])) else None,

                    int(row["volume_lag_1"]) if row["volume_lag_1"] == row["volume_lag_1"] else None,
                    int(row["volume_lag_5"]) if row["volume_lag_5"] == row["volume_lag_5"] else None,

                    float(row["open_lag_1"]) if row["open_lag_1"] == row["open_lag_1"] else None,
                    float(row["high_lag_1"]) if row["high_lag_1"] == row["high_lag_1"] else None,
                    float(row["low_lag_1"]) if row["low_lag_1"] == row["low_lag_1"] else None,

                    float(row["rolling_mean_20"]) if row["rolling_mean_20"] == row["rolling_mean_20"] else None,
                    float(row["rolling_std_20"]) if row["rolling_std_20"] == row["rolling_std_20"] else None,
                    float(row["rolling_max_20"]) if row["rolling_max_20"] == row["rolling_max_20"] else None,
                    float(row["rolling_min_20"]) if row["rolling_min_20"] == row["rolling_min_20"] else None,
                    float(row["rolling_median_20"]) if row["rolling_median_20"] == row["rolling_median_20"] else None
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
    print(" Processed Data Loaded Successfully!")