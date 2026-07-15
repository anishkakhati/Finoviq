import yfinance as yf

from backend.data_pipeline.transform import transform_data
from backend.data_pipeline.validate import validate_data


def download_stock(symbol):

    print(f"Downloading {symbol}...")

    data = yf.Ticker(symbol).history(period="1y")

    return data


if __name__ == "__main__":

    apple = download_stock("AAPL")

    transformed = transform_data(apple)

    validate_data(transformed)