"""
Finoviq AI - Confidence Score Module

Calculates a confidence score based on
technical indicators and prediction agreement.
"""

from typing import Dict


def calculate_confidence(
    predicted_close: float,
    current_close: float,
    rsi: float,
    macd: float,
    trend_strength: float,
    volatility: str,
) -> Dict:
    """
    Calculate confidence score for a trade.
    """

    score = 0
    reasons = []

    # Bullish Prediction
    if predicted_close > current_close:
        score += 35
        reasons.append("Bullish prediction")

    # RSI
    if 40 <= rsi <= 60:
        score += 20
        reasons.append("Healthy RSI")

    elif rsi < 40:
        score += 15
        reasons.append("Oversold RSI")

    # MACD
    if macd > 0:
        score += 20
        reasons.append("Positive MACD")

    # Trend Strength
    if trend_strength >= 1.2:
        score += 15
        reasons.append("Strong trend")

    elif trend_strength >= 1.0:
        score += 10
        reasons.append("Moderate trend")

    # Volatility
    volatility = volatility.lower()

    if volatility == "low":
        score += 10
        reasons.append("Low volatility")

    elif volatility == "medium":
        score += 5
        reasons.append("Medium volatility")

    score = min(score, 100)

    return {
        "confidence": score,
        "reason": ", ".join(reasons)
    }


if __name__ == "__main__":

    result = calculate_confidence(
        predicted_close=263.20,
        current_close=250.00,
        rsi=45,
        macd=1.5,
        trend_strength=1.25,
        volatility="medium",
    )

    print(result)