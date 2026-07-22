from datetime import date


def generate_prediction_report(
    company_id,
    prediction,
    model_name,
    confidence
):
    """
    Display a professional prediction report.
    """

    print("\n")
    print("=" * 60)
    print("              FINOVIQ AI MARKET FORECAST")
    print("=" * 60)

    print(f"\nPrediction Date : {date.today()}")
    print(f"Company ID      : {company_id}")

    print("\nTomorrow Forecast")
    print("-" * 35)

    print(f"Open  : ₹{prediction['open']:.2f}")
    print(f"High  : ₹{prediction['high']:.2f}")
    print(f"Low   : ₹{prediction['low']:.2f}")
    print(f"Close : ₹{prediction['close']:.2f}")

    print("\nExpected Range")
    print("-" * 35)

    expected_range = prediction["high"] - prediction["low"]

    print(f"₹{expected_range:.2f}")

    print("\nModel Used")
    print("-" * 35)

    print(model_name)

    print("\nPrediction Confidence")
    print("-" * 35)

    print(f"{confidence * 100:.1f}%")

    print("\nPrediction saved into PostgreSQL ✓")

    print("\n")
    print("=" * 60)