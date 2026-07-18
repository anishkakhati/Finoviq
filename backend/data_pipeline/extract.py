import yfinance as yf

from backend.data_pipeline.transform import transform_data
from backend.data_pipeline.validate import validate_data
from backend.data_pipeline.load import load_data

from backend.feature_engineering.feature_builder import build_features

from backend.database.db import get_company_id


def download_stock(symbol):
    """
    Download historical stock data from Yahoo Finance.
    """

    print(f"\n========== DOWNLOADING {symbol} ==========\n")

    data = yf.Ticker(symbol).history(period="1y")

    return data


if __name__ == "__main__":

    print("\n========== FINOVIQ AI ETL PIPELINE ==========\n")

    # Stocks to process
    symbols = [
        "AAPL",
        "MSFT",
        "TSLA",
        "GOOGL",
        "AMZN"
    ]

    for symbol in symbols:

        print("\n" + "=" * 60)
        print(f"Processing {symbol}")
        print("=" * 60)

        # STEP 1 — Get Company ID
        company_id = get_company_id(symbol)

        if company_id is None:
            print(f"{symbol} not found in companies table.")
            continue

        # STEP 2 — Extract Data
        raw_data = download_stock(symbol)

        # STEP 3 — Transform Data
        transformed_data = transform_data(raw_data, company_id)

        # STEP 4 — Validate Raw Data
        if not validate_data(transformed_data):
            print(f"Validation failed for {symbol}.")
            continue

        # STEP 5 — Complete Feature Engineering Pipeline
        processed_data = build_features(transformed_data)

        # STEP 6 — Load into PostgreSQL
        load_data(processed_data)

        print(f"\n{symbol} pipeline completed successfully.")

    print("\n========== ETL PIPELINE FINISHED SUCCESSFULLY ==========\n")