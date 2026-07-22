import pandas as pd


def create_targets(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["target_open"] = (
        df.groupby("company_id")["open"]
        .shift(-1)
    )

    df["target_high"] = (
        df.groupby("company_id")["high"]
        .shift(-1)
    )

    df["target_low"] = (
        df.groupby("company_id")["low"]
        .shift(-1)
    )

    df["target_close"] = (
        df.groupby("company_id")["close"]
        .shift(-1)
    )

    df.reset_index(drop=True, inplace=True)

    return df