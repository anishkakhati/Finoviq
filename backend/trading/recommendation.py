"""
Finoviq AI - Recommendation Module

Generates the final trading recommendation
using confidence score, ROI, and entry signal.
"""

from typing import Dict


def generate_recommendation(
    entry_signal: str,
    confidence: int,
    expected_roi: float,
) -> Dict:
    """
    Generate BUY, HOLD, or SELL recommendation.
    """

    if not (0 <= confidence <= 100):
        raise ValueError("Confidence must be between 0 and 100.")

    recommendation = "HOLD"
    reason = "Market conditions are uncertain."

    if (
        entry_signal == "BUY"
        and confidence >= 80
        and expected_roi >= 5
    ):
        recommendation = "BUY"
        reason = "High confidence with attractive expected return."

    elif (
        entry_signal == "BUY"
        and 60 <= confidence < 80
    ):
        recommendation = "HOLD"
        reason = "Good opportunity, but confirmation is recommended."

    elif confidence < 60:
        recommendation = "SELL"
        reason = "Low confidence. Avoid taking this trade."

    return {
        "recommendation": recommendation,
        "confidence": confidence,
        "expected_roi": round(expected_roi, 2),
        "reason": reason,
    }


if __name__ == "__main__":

    result = generate_recommendation(
        entry_signal="BUY",
        confidence=87,
        expected_roi=5.8,
    )

    print(result)