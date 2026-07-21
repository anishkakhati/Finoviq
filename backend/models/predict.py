import joblib
import pandas as pd

# ==========================================
# LOAD BEST MODEL
# ==========================================

model = joblib.load(
    "backend/saved_models/best_model.pkl"
)

# ==========================================
# LOAD SCALER
# ==========================================

scaler = joblib.load(
    "backend/saved_models/scaler.pkl"
)

# ==========================================
# LOAD FEATURE ORDER
# ==========================================

feature_columns = joblib.load(
    "backend/saved_models/feature_columns.pkl"
)


def predict_next_day(stock_data):

    # ==========================================
    # CREATE DATAFRAME
    # ==========================================

    data = pd.DataFrame([stock_data])

    # ==========================================
    # REORDER COLUMNS
    # ==========================================

    data = data[feature_columns]

    print("\n========== INPUT DATA ==========\n")
    print(data)

    # ==========================================
    # SCALE FEATURES
    # ==========================================

    scaled = scaler.transform(data)

    print("\n========== SCALED DATA ==========\n")
    print(scaled)

    # ==========================================
    # MAKE PREDICTION
    # ==========================================

    prediction = model.predict(scaled)

    print("\n========== PREDICTION ==========\n")
    print(f"Predicted Tomorrow Close Price : {prediction[0]:.2f}")

    return float(prediction[0])