import pandas as pd


def transform_data(data):
    """
    Transform raw stock data into a clean format
    ready to be stored in PostgreSQL.
    """

    print("\n========== TRANSFORMING DATA ==========\n")

    data = data.dropna()

    data = data.reset_index()

    data = data.rename(columns={
        "Date": "trade_date",
        "Open": "open_price",
        "High": "high_price",
        "Low": "low_price",
        "Close": "close_price",
        "Volume": "volume",
        "Dividends": "dividends",
        "Stock Splits": "stock_splits"
    })

   
    data = data[
        [
            "trade_date",
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume"
        ]
    ]

    data = data.sort_values(
        by="trade_date",
        ascending=True
    )

    data["trade_date"] = pd.to_datetime(data["trade_date"])

    print(data.head())

    print("\n✅ Transformation Complete!\n")

    return data