from backend.feature_engineering.preprocessing import preprocess_data
from backend.feature_engineering.indicators import add_indicators
from backend.feature_engineering.lag_features import add_lag_features
from backend.feature_engineering.validator import validate_features


def build_features(data):

    print("\n========== FEATURE ENGINEERING PIPELINE ==========\n")

    data = preprocess_data(data)

    data = add_indicators(data)

    data = add_lag_features(data)

    validate_features(data)

    return data