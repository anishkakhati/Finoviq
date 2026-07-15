import yfinance as yf

from backend.data_pipeline.transform import transform_data
from backend.data_pipeline.validate import validate_data
from backend.data_pipeline.load import load_data

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

        # Get company ID from PostgreSQL
        company_id = get_company_id(symbol)

        if company_id is None:
            print(f" {symbol} not found in companies table.")
            continue

        # STEP 1 - Extract
        data = download_stock(symbol)

        # STEP 2 - Transform
        transformed = transform_data(data, company_id)

        # STEP 3 - Validate
        if validate_data(transformed):

            # STEP 4 - Load
            load_data(transformed)

            print(f" {symbol} pipeline completed successfully.")

        else:
            print(f" Validation failed for {symbol}. Data not loaded.")

    print("\n ETL Pipeline Finished Successfully!")