import yfinance as yf

from backend.data_pipeline.transform import transform_data
from backend.data_pipeline.validate import validate_data
from backend.data_pipeline.load import load_data

from backend.feature_engineering.preprocessing import preprocess_data
from backend.feature_engineering.indicators import add_indicators
from backend.feature_engineering.lag_features import add_lag_features

from backend.database.db import get_company_id


def download_stock(symbol):
    """
    Download historical stock data from Yahoo Finance.
    """

    print(f"\nDownloading {symbol}...")

    data = yf.Ticker(symbol).history(period="1y")

    return data


if __name__ == "__main__":

    # List of stocks to download
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
            print(f" {symbol} not found in companies table.")
            continue

        # STEP 2 — Extract
        data = download_stock(symbol)

        # STEP 3 — Transform
        transformed = transform_data(data, company_id)

        # STEP 4 — Validate
        if validate_data(transformed):

            # STEP 5 — Preprocess
            processed = preprocess_data(transformed)

            # STEP 6 — Technical Indicators
            processed = add_indicators(processed)

            # STEP 7 — Lag Features
            processed = add_lag_features(processed)

            # STEP 8 — Load to PostgreSQL
            load_data(processed)

            print(f" {symbol} pipeline completed successfully.")

        else:
            print(f" Validation failed for {symbol}. Data not loaded.")

    print("\n ETL Pipeline Finished Successfully!")