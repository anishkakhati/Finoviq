"""
Finoviq AI - Take Profit Module

Calculates the take-profit target using
entry price, stop loss, and risk-reward ratio.
"""

from typing import Dict


def calculate_take_profit(
    entry_price: float,
    stop_loss: float,
    risk_reward_ratio: float = 3.0,
) -> Dict:
    """
    Calculate the recommended take-profit price.
    """

    if entry_price <= 0:
        raise ValueError("Entry price must be greater than zero.")

    if stop_loss <= 0:
        raise ValueError("Stop loss must be greater than zero.")

    if stop_loss >= entry_price:
        raise ValueError("Stop loss must be below entry price.")

    if risk_reward_ratio <= 0:
        raise ValueError("Risk reward ratio must be greater than zero.")

    risk = entry_price - stop_loss
    reward = risk * risk_reward_ratio

    take_profit = entry_price + reward

    expected_return = (reward / entry_price) * 100

    return {
        "take_profit": round(take_profit, 2),
        "risk": round(risk, 2),
        "reward": round(reward, 2),
        "risk_reward_ratio": risk_reward_ratio,
        "expected_return": round(expected_return, 2),
        "reason": f"Calculated using 1:{risk_reward_ratio} Risk-Reward ratio."
    }


if __name__ == "__main__":

    result = calculate_take_profit(
        entry_price=248.80,
        stop_loss=244.00,
        risk_reward_ratio=3
    )

    print(result)