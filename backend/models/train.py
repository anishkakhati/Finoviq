import os
import time
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputRegressor

from backend.models.preprocessing import load_dataset
from backend.models.evaluate import evaluate_model
from backend.database.save_results import save_model_results


def train_model():

    print("\n========== TRAINING MULTI-OUTPUT LINEAR REGRESSION ==========\n")

    # ==========================================================
    # LOAD DATASET
    # ==========================================================

    X, y, data = load_dataset(model_type="linear")

    # ==========================================================
    # TRAIN TEST SPLIT
    # ==========================================================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        shuffle=False
    )

    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    # ==========================================================
    # FEATURE SCALING
    # ==========================================================

    print("\n========== SCALING FEATURES ==========\n")

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("Feature Scaling Completed!")

    # ==========================================================
    # TRAIN MODEL
    # ==========================================================

    print("\n========== TRAINING MULTI-OUTPUT LINEAR REGRESSION ==========\n")

    model = MultiOutputRegressor(
        LinearRegression()
    )

    start = time.time()

    model.fit(X_train, y_train)

    training_time = time.time() - start

    # ==========================================================
    # CHECK FIRST TRAINING SAMPLE
    # ==========================================================

    print("\n========== FIRST TRAINING SAMPLE ==========\n")

    prediction = model.predict([X_train[0]])[0]

    print("Prediction:")
    print(prediction)

    print("\nActual:")
    print(y_train.iloc[0].values)

    # ==========================================================
    # MODEL COEFFICIENTS
    # ==========================================================

    target_names = [
        "Open",
        "High",
        "Low",
        "Close"
    ]

    print("\n========== MODEL COEFFICIENTS ==========\n")

    for target_name, estimator in zip(
        target_names,
        model.estimators_
    ):

        print(f"\n------ {target_name} ------")

        for feature, coef in zip(
            X.columns,
            estimator.coef_
        ):

            print(f"{feature:<25} {coef:>12.4f}")

        print(f"Intercept : {estimator.intercept_:.4f}")

    # ==========================================================
    # SAVE MODEL
    # ==========================================================

    os.makedirs(
        "backend/saved_models",
        exist_ok=True
    )

    joblib.dump(
        model,
        "backend/saved_models/multi_linear_regression.pkl"
    )

    joblib.dump(
        scaler,
        "backend/saved_models/scaler.pkl"
    )

    joblib.dump(
        list(X.columns),
        "backend/saved_models/feature_columns.pkl"
    )

    print("\nMulti-Output Model Saved Successfully!")

    # ==========================================================
    # TEST PREDICTIONS
    # ==========================================================

    predictions = model.predict(X_test)

    print("\n========== FIRST 10 PREDICTIONS ==========\n")

    for i in range(10):

        print(f"\nSample {i+1}")

        print("Actual:")
        print(y_test.iloc[i].values)

        print("Predicted:")
        print(predictions[i])

    # ==========================================================
    # EVALUATION
    # ==========================================================

    metrics = evaluate_model(
        y_true=y_test,
        predictions=predictions,
        model_name="Multi-Output Linear Regression"
    )

    # ==========================================================
    # SAVE RESULTS
    # ==========================================================

    save_model_results(
        model_name="Multi-Output Linear Regression",
        mae=metrics["mae"],
        rmse=metrics["rmse"],
        r2=metrics["r2"],
        mape=metrics["mape"],
        training_time=training_time
    )

    # ==========================================================
    # PREDICTION STATISTICS
    # ==========================================================

    print("\n========== PREDICTION STATISTICS ==========\n")

    print("Prediction Shape :", predictions.shape)
    print("NaN Values       :", np.isnan(predictions).any())
    print("Infinite Values  :", np.isinf(predictions).any())

    return (
        model,
        scaler,
        X_train,
        X_test,
        y_train,
        y_test,
        predictions,
        metrics
    )


if __name__ == "__main__":

    train_model()