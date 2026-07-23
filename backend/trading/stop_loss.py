"""
Finoviq AI - Stop Loss Module

Calculates a dynamic stop-loss based on
entry price, ATR, and market volatility.
"""

from typing import Dict


def calculate_stop_loss(
    entry_price: float,
    atr: float,
    volatility: str = "medium",
) -> Dict:
    """
    Calculate the recommended stop-loss price.
    """

    if entry_price <= 0:
        raise ValueError("Entry price must be greater than zero.")

    if atr <= 0:
        raise ValueError("ATR must be greater than zero.")

    volatility = volatility.lower()

    multipliers = {
        "low": 1.0,
        "medium": 1.5,
        "high": 2.0,
    }

    multiplier = multipliers.get(volatility, 1.5)

    stop_loss = entry_price - (atr * multiplier)

    risk_per_share = entry_price - stop_loss
    risk_percentage = (risk_per_share / entry_price) * 100

    return {
        "stop_loss": round(stop_loss, 2),
        "risk_per_share": round(risk_per_share, 2),
        "risk_percentage": round(risk_percentage, 2),
        "multiplier": multiplier,
        "reason": f"{volatility.capitalize()} volatility ATR-based stop loss."
    }


if __name__ == "__main__":

    result = calculate_stop_loss(
        entry_price=248.80,
        atr=3.20,
        volatility="medium",
    )

    print(result)