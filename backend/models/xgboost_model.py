import os
import time
import joblib
import numpy as np

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor

from backend.models.preprocessing import load_dataset
from backend.models.evaluate import evaluate_model
from backend.database.save_results import save_model_results


def train_xgboost():

    print("\n========== TRAINING MULTI-OUTPUT XGBOOST ==========\n")

    # ==========================================================
    # LOAD DATASET
    # ==========================================================

    X, y, data = load_dataset(model_type="tree")

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
    # CREATE MULTI-OUTPUT XGBOOST
    # ==========================================================

    model = MultiOutputRegressor(

        XGBRegressor(

            objective="reg:squarederror",

            n_estimators=500,

            learning_rate=0.05,

            max_depth=6,

            subsample=0.8,

            colsample_bytree=0.8,

            random_state=42,

            n_jobs=-1

        )

    )

    # ==========================================================
    # TRAIN MODEL
    # ==========================================================

    print("\nTraining Multi-Output XGBoost...\n")

    start = time.time()

    model.fit(
        X_train,
        y_train
    )

    training_time = time.time() - start

    print("Training Completed!")

    print(f"Training Time : {training_time:.2f} seconds")

    # ==========================================================
    # MAKE PREDICTIONS
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
    # EVALUATE MODEL
    # ==========================================================

    metrics = evaluate_model(

        y_true=y_test,

        predictions=predictions,

        model_name="Multi-Output XGBoost"

    )

    # ==========================================================
    # SAVE RESULTS
    # ==========================================================

    save_model_results(

        model_name="Multi-Output XGBoost",

        mae=metrics["mae"],

        rmse=metrics["rmse"],

        r2=metrics["r2"],

        mape=metrics["mape"],

        training_time=training_time

    )

    # ==========================================================
    # FEATURE IMPORTANCE
    # ==========================================================

    print("\n========== FEATURE IMPORTANCE ==========\n")

    feature_importance = np.mean(

        [

            estimator.feature_importances_

            for estimator in model.estimators_

        ],

        axis=0

    )

    feature_importance = sorted(

        zip(X.columns, feature_importance),

        key=lambda x: x[1],

        reverse=True

    )

    for feature, score in feature_importance:

        print(f"{feature:<25} {score:.6f}")

    # ==========================================================
    # SAVE MODEL
    # ==========================================================

    os.makedirs(

        "backend/saved_models",

        exist_ok=True

    )

    joblib.dump(

        model,

        "backend/saved_models/multi_xgboost.pkl"

    )

    print("\nMulti-Output XGBoost Model Saved Successfully!")

    # ==========================================================
    # PREDICTION STATISTICS
    # ==========================================================

    print("\n========== PREDICTION STATISTICS ==========\n")

    print("Prediction Shape :", predictions.shape)

    print("NaN Values       :", np.isnan(predictions).any())

    print("Infinite Values  :", np.isinf(predictions).any())

    return (

        model,

        predictions,

        y_test,

        metrics,

        training_time

    )


if __name__ == "__main__":

    train_xgboost()