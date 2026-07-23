""" 
Rule 1

If: prediction is bullish
    RSI is below 45
    MACD is bullish

➡ Buy near the predicted low.

Rule 2

If: prediction is bullish
    RSI is neutral

➡ Buy near the predicted open.

Rule 3

If: prediction is bearish

➡ Don't buy.

"""


from typing import Dict


def generate_entry_signal(
    predicted_open: float,
    predicted_high: float,
    predicted_low: float,
    predicted_close: float,
    current_close: float,
    rsi: float,
    macd: float,
    atr: float,
) -> Dict:
    """
    Generate BUY or WAIT signal with suggested entry price.
    """

    # Basic validation
    prices = [
        predicted_open,
        predicted_high,
        predicted_low,
        predicted_close,
        current_close,
    ]

    if any(price <= 0 for price in prices):
        raise ValueError("All prices must be greater than zero.")

    if not (0 <= rsi <= 100):
        raise ValueError("RSI must be between 0 and 100.")

    bullish_prediction = predicted_close > current_close

    # Strong Buy
    if bullish_prediction and rsi < 45 and macd > 0:
        return {
            "signal": "BUY",
            "entry_price": round(predicted_low, 2),
            "reason": "Bullish trend with oversold RSI and positive MACD."
        }

    # Moderate Buy
    if bullish_prediction and 45 <= rsi <= 60 and macd > 0:
        entry_price = min(predicted_open, current_close)

        return {
            "signal": "BUY",
            "entry_price": round(entry_price, 2),
            "reason": "Bullish trend with healthy RSI."
        }

    # Weak Bullish
    if bullish_prediction and macd <= 0:
        return {
            "signal": "WAIT",
            "entry_price": None,
            "reason": "Bullish prediction but MACD is not supportive."
        }

    # Overbought Market
    if bullish_prediction and rsi > 70:
        return {
            "signal": "WAIT",
            "entry_price": None,
            "reason": "RSI indicates overbought conditions."
        }

    # Bearish Market
    return {
        "signal": "WAIT",
        "entry_price": None,
        "reason": "Bearish prediction. No safe entry available."
    }


if __name__ == "__main__":

    result = generate_entry_signal(
        predicted_open=251.2,
        predicted_high=266.5,
        predicted_low=248.8,
        predicted_close=263.4,
        current_close=250.0,
        rsi=41.5,
        macd=1.8,
        atr=3.2,
    )

    print(result)