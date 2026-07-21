import os
import shutil

from backend.models.train import train_model
from backend.models.random_forest import train_random_forest
from backend.models.xgboost_model import train_xgboost


def compare_models():

    print("\n")
    print("=" * 60)
    print("          FINOVIQ AI MODEL COMPARISON")
    print("=" * 60)

    # ==========================================
    # Train All Models
    # ==========================================

    _, _, _, _, _, _, _, linear_metrics = train_model()

    _, _, _, rf_metrics, _ = train_random_forest()

    _, _, _, xgb_metrics, _ = train_xgboost()

    models = [

        linear_metrics,

        rf_metrics,

        xgb_metrics

    ]

    # ==========================================
    # Sort Models
    # ==========================================

    models = sorted(

        models,

        key=lambda x: x["r2"],

        reverse=True

    )

    print("\n")
    print("=" * 75)

    print(
        f'{"MODEL":<22}'
        f'{"MAE":>10}'
        f'{"RMSE":>10}'
        f'{"R²":>10}'
        f'{"MAPE":>12}'
    )

    print("=" * 75)

    for model in models:

        print(

            f'{model["model"]:<22}'
            f'{model["mae"]:>10.4f}'
            f'{model["rmse"]:>10.4f}'
            f'{model["r2"]:>10.4f}'
            f'{model["mape"]:>11.2f}%'

        )

    print("=" * 75)

    best_model = models[0]["model"]

    print(f"\n🏆 BEST MODEL : {best_model}")

    # ==========================================
    # Save Best Model
    # ==========================================

    if best_model == "Linear Regression":

        shutil.copy(

            "backend/saved_models/linear_regression.pkl",

            "backend/saved_models/best_model.pkl"

        )

    elif best_model == "Random Forest":

        shutil.copy(

            "backend/saved_models/random_forest.pkl",

            "backend/saved_models/best_model.pkl"

        )

    else:

        shutil.copy(

            "backend/saved_models/xgboost.pkl",

            "backend/saved_models/best_model.pkl"

        )

    print("\nBest model saved as")

    print("backend/saved_models/best_model.pkl")


if __name__ == "__main__":

    compare_models()