"""
Finoviq AI - Profit Calculator Module

Calculates investment metrics including shares,
expected profit, expected loss, and ROI.
"""

from typing import Dict


def calculate_profit(
    investment: float,
    entry_price: float,
    exit_price: float,
    stop_loss: float,
) -> Dict:
    """
    Calculate expected profit and loss.
    """

    if investment <= 0:
        raise ValueError("Investment must be greater than zero.")

    if entry_price <= 0:
        raise ValueError("Entry price must be greater than zero.")

    if exit_price <= 0:
        raise ValueError("Exit price must be greater than zero.")

    if stop_loss <= 0:
        raise ValueError("Stop loss must be greater than zero.")

    if stop_loss >= entry_price:
        raise ValueError("Stop loss must be below entry price.")

    shares = int(investment // entry_price)

    invested_amount = shares * entry_price

    expected_profit = shares * (exit_price - entry_price)

    expected_loss = shares * (entry_price - stop_loss)

    roi = (expected_profit / invested_amount) * 100

    loss_percentage = (expected_loss / invested_amount) * 100

    return {
        "investment": round(investment, 2),
        "shares": shares,
        "invested_amount": round(invested_amount, 2),
        "entry_price": round(entry_price, 2),
        "exit_price": round(exit_price, 2),
        "stop_loss": round(stop_loss, 2),
        "expected_profit": round(expected_profit, 2),
        "expected_loss": round(expected_loss, 2),
        "roi": round(roi, 2),
        "loss_percentage": round(loss_percentage, 2),
    }


if __name__ == "__main__":

    result = calculate_profit(
        investment=100000,
        entry_price=248.80,
        exit_price=263.20,
        stop_loss=244.00,
    )

    print(result)