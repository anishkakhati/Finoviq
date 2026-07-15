import pandas as pd


def validate_data(data):

    print("\n========== DATA VALIDATION ==========\n")

    # Missing values
    missing = data.isnull().sum()

    print("Missing Values:")
    print(missing)

    if missing.sum() > 0:
        print("\n❌ Validation Failed: Missing values found.")
        return False

    # Duplicate rows
    duplicates = data.duplicated().sum()

    print(f"\nDuplicate Rows: {duplicates}")

    if duplicates > 0:
        print("❌ Validation Failed: Duplicate rows found.")
        return False

    # Negative prices
    price_columns = [
        "open_price",
        "high_price",
        "low_price",
        "close_price"
    ]

    for column in price_columns:

        negative = (data[column] < 0).sum()

        print(f"Negative values in {column}: {negative}")

        if negative > 0:
            print(f"❌ Validation Failed: Negative values in {column}.")
            return False

    # Data Types
    print("\nData Types:")
    print(data.dtypes)

    print("\n✅ Validation Passed!")

    return True