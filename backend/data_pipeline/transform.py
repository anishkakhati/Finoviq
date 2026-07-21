import pandas as pd


def transform_data(data, company_id):

    print("\n========== TRANSFORMING DATA ==========\n")

    # Remove missing values
    data = data.dropna()

    # Reset index (Date becomes a normal column)
    data = data.reset_index()

    # Rename columns
    data = data.rename(columns={
        "Date": "trade_date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    # Keep only required columns
    data = data[
        [
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "volume"
        ]
    ]

    # Add company_id
    data["company_id"] = company_id


    # Sort by date
    data = data.sort_values("trade_date")

    # Correct data types
    data["trade_date"] = pd.to_datetime(data["trade_date"])
    data["company_id"] = data["company_id"].astype(int)

    print(data.head())

    print("\nTransformation Complete!\n")

    return data