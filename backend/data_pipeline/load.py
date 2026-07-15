import psycopg2

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


def load_data(data):

    print("\n========== LOADING DATA ==========\n")

    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cursor = connection.cursor()

    insert_query = """
    INSERT INTO stock_prices
    (
        company_id,
        trade_date,
        open,
        high,
        low,
        close,
        adj_close,
        volume
    )
    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,%s
    )
    ON CONFLICT (company_id, trade_date)
    DO NOTHING;
    """

    for _, row in data.iterrows():

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
                int(row["volume"])
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("Data Loaded Successfully!")