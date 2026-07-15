import pandas as pd


def validate_data(data):

    print("\n========== DATA VALIDATION ==========\n")

    missing = data.isnull().sum()

    print("Missing Values:")
    print(missing)

    if missing.sum() > 0:
        print("\nValidation Failed: Missing values found.")
        return False

    # -------------------------------
    # Check Duplicate Rows
    # -------------------------------
    duplicates = data.duplicated().sum()

    print(f"\nDuplicate Rows: {duplicates}")

    if duplicates > 0:
        print(" Validation Failed: Duplicate rows found.")
        return False

    # -------------------------------
    # Check Negative Prices
    # -------------------------------
    price_columns = [
        "open",
        "high",
        "low",
        "close"
    ]

    for column in price_columns:

        negative = (data[column] < 0).sum()

        print(f"Negative values in {column}: {negative}")

        if negative > 0:
            print(f" Validation Failed: Negative values in {column}.")
            return False

    # -------------------------------
    # Check Data Types
    # -------------------------------
    print("\nData Types:")
    print(data.dtypes)

    # -------------------------------
    # Validation Passed
    # -------------------------------
    print("\n Validation Passed!")

    return True