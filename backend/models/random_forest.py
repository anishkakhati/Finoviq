import os
import time
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

from backend.models.preprocessing import load_dataset
from backend.models.evaluate import evaluate_model
from backend.database.save_results import save_model_results


def train_random_forest():

    print("\n========== RANDOM FOREST TRAINING ==========\n")

    # ==========================================================
    # LOAD DATASET
    # ==========================================================

    X, y, data = load_dataset(model_type="tree")

    # ==========================================================
    # TRAIN TEST SPLIT (TIME SERIES)
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
    # CREATE RANDOM FOREST MODEL
    # ==========================================================

    model = RandomForestRegressor(

        n_estimators=300,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1

    )

    # ==========================================================
    # TRAIN MODEL
    # ==========================================================

    print("\nTraining Random Forest...\n")

    start = time.time()

    model.fit(X_train, y_train)

    training_time = time.time() - start

    print("Training Completed!")

    print(f"Training Time : {training_time:.2f} seconds")

    # ==========================================================
    # PREDICTIONS
    # ==========================================================

    predictions = model.predict(X_test)

    print("\n========== FIRST 10 PREDICTIONS ==========\n")

    for actual, predicted in zip(
        y_test.iloc[:10],
        predictions[:10]
    ):

        print(
            f"Actual : {actual:.2f}     Predicted : {predicted:.2f}"
        )

    # ==========================================================
    # EVALUATION
    # ==========================================================

    metrics = evaluate_model(

        y_true=y_test,

        predictions=predictions,

        model_name="Random Forest"

    )

    # ==========================================================
    # SAVE RESULTS TO POSTGRESQL
    # ==========================================================

    save_model_results(

        model_name="Random Forest",

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

    importance = model.feature_importances_

    feature_importance = sorted(

        zip(X.columns, importance),

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

        "backend/saved_models/random_forest.pkl"

    )

    print("\nRandom Forest Model Saved Successfully!")

    return (

        model,

        predictions,

        y_test,

        metrics,

        training_time

    )


if __name__ == "__main__":

    train_random_forest()