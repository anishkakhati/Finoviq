"""
Finoviq AI - Exit Strategy Module

Determines the final exit price by combining
model predictions with the take-profit target.
"""

from typing import Dict


def generate_exit_signal(
    predicted_high: float,
    predicted_close: float,
    take_profit: float,
    trend_strength: float = 1.0,
) -> Dict:
    """
    Generate the final exit price.
    """

    prices = [
        predicted_high,
        predicted_close,
        take_profit,
    ]

    if any(price <= 0 for price in prices):
        raise ValueError("All prices must be greater than zero.")

    if trend_strength <= 0:
        raise ValueError("Trend strength must be positive.")

    # ----------------------------------------------------
    # Strong bullish trend
    # Hold longer, but never exceed predicted high
    # ----------------------------------------------------

    if trend_strength >= 1.2:

        exit_price = min(predicted_high, take_profit)

        reason = (
            "Strong bullish trend. "
            "Targeting minimum of predicted high and take-profit."
        )

    # ----------------------------------------------------
    # Moderate trend
    # ----------------------------------------------------

    elif trend_strength >= 1.0:

        average_price = (predicted_high + predicted_close) / 2

        exit_price = min(average_price, take_profit)

        reason = (
            "Moderate trend. "
            "Using average prediction capped by take-profit."
        )

    # ----------------------------------------------------
    # Weak trend
    # ----------------------------------------------------

    else:

        exit_price = min(predicted_close, take_profit)

        reason = (
            "Weak trend. "
            "Exiting near predicted close."
        )

    return {

        "exit_price": round(exit_price, 2),

        "reason": reason

    }


if __name__ == "__main__":

    result = generate_exit_signal(

        predicted_high=266.5,

        predicted_close=263.4,

        take_profit=263.2,

        trend_strength=1.25,

    )

    print(result)