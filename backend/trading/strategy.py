"""
Finoviq AI - Trading Strategy Engine
"""

from .entry_strategy import generate_entry_signal
from .stop_loss import calculate_stop_loss
from .take_profit import calculate_take_profit
from .exit_strategy import generate_exit_signal
from .profit_calculator import calculate_profit
from .confidence import calculate_confidence
from .recommendation import generate_recommendation


def generate_trade_strategy(

    predicted_open,
    predicted_high,
    predicted_low,
    predicted_close,

    current_close,

    rsi,
    macd,
    atr,

    trend_strength,

    volatility,

    investment,

):

    # ==================================================
    # STEP 1
    # Entry Strategy
    # ==================================================

    entry = generate_entry_signal(

        predicted_open=predicted_open,

        predicted_high=predicted_high,

        predicted_low=predicted_low,

        predicted_close=predicted_close,

        current_close=current_close,

        rsi=rsi,

        macd=macd,

        atr=atr,

    )

    if entry["signal"] != "BUY":

        return {

            "recommendation": "WAIT",

            "reason": entry["reason"]

        }

    entry_price = entry["entry_price"]

    # ==================================================
    # STEP 2
    # Stop Loss
    # ==================================================

    stop = calculate_stop_loss(

        entry_price=entry_price,

        atr=atr,

        volatility=volatility,

    )

    stop_loss = stop["stop_loss"]

    # ==================================================
    # STEP 3
    # Take Profit
    # ==================================================

    take_profit = calculate_take_profit(

        entry_price=entry_price,

        stop_loss=stop_loss,

    )

    take_profit_price = take_profit["take_profit"]

    # ==================================================
    # STEP 4
    # Exit Strategy
    # ==================================================

    exit_signal = generate_exit_signal(

        predicted_high=predicted_high,

        predicted_close=predicted_close,

        take_profit=take_profit_price,

        trend_strength=trend_strength,

    )

    exit_price = exit_signal["exit_price"]

    # ==================================================
    # STEP 5
    # Profit Calculator
    # ==================================================

    profit = calculate_profit(

        investment=investment,

        entry_price=entry_price,

        exit_price=exit_price,

        stop_loss=stop_loss,

    )

    # ==================================================
    # STEP 6
    # Confidence
    # ==================================================

    confidence = calculate_confidence(

        predicted_close=predicted_close,

        current_close=current_close,

        rsi=rsi,

        macd=macd,

        trend_strength=trend_strength,

        volatility=volatility,

    )

    # ==================================================
    # STEP 7
    # Recommendation
    # ==================================================

    recommendation = generate_recommendation(

        entry_signal=entry["signal"],

        confidence=confidence["confidence"],

        expected_roi=profit["roi"],

    )

    # ==================================================
    # FINAL RESULT
    # ==================================================

    return {

        "entry": entry,

        "stop_loss": stop,

        "take_profit": take_profit,

        "exit": exit_signal,

        "profit": profit,

        "confidence": confidence,

        "recommendation": recommendation,

    }


if __name__ == "__main__":

    from pprint import pprint

    result = generate_trade_strategy(

        predicted_open=251.2,

        predicted_high=266.5,

        predicted_low=248.8,

        predicted_close=263.4,

        current_close=250,

        rsi=42,

        macd=1.8,

        atr=3.2,

        trend_strength=1.25,

        volatility="medium",

        investment=100000,

    )

    pprint(result)