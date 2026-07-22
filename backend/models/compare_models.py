import os
import shutil

from backend.models.train import train_model
from backend.models.random_forest import train_random_forest
from backend.models.xgboost_model import train_xgboost


def compare_models():

    print("\n")
    print("=" * 80)
    print("               FINOVIQ AI MODEL COMPARISON")
    print("=" * 80)

    # ==========================================================
    # TRAIN ALL MODELS
    # ==========================================================

    print("\nTraining Multi-Output Linear Regression...\n")

    (
        _,
        _,
        _,
        _,
        _,
        _,
        _,
        linear_metrics

    ) = train_model()

    print("\nTraining Multi-Output Random Forest...\n")

    (
        _,
        _,
        _,
        rf_metrics,
        _

    ) = train_random_forest()

    print("\nTraining Multi-Output XGBoost...\n")

    (
        _,
        _,
        _,
        xgb_metrics,
        _

    ) = train_xgboost()

    # ==========================================================
    # STORE RESULTS
    # ==========================================================

    models = [

        linear_metrics,

        rf_metrics,

        xgb_metrics

    ]

    # ==========================================================
    # SORT BY R²
    # ==========================================================

    models = sorted(

        models,

        key=lambda x: x["r2"],

        reverse=True

    )

    # ==========================================================
    # DISPLAY RESULTS
    # ==========================================================

    print("\n")
    print("=" * 95)

    print(

        f'{"Rank":<6}'
        f'{"Model":<35}'
        f'{"MAE":>10}'
        f'{"RMSE":>12}'
        f'{"R²":>12}'
        f'{"MAPE":>12}'

    )

    print("=" * 95)

    for rank, model in enumerate(models, start=1):

        print(

            f'{rank:<6}'
            f'{model["model"]:<35}'
            f'{model["mae"]:>10.4f}'
            f'{model["rmse"]:>12.4f}'
            f'{model["r2"]:>12.4f}'
            f'{model["mape"]:>11.2f}%'

        )

    print("=" * 95)

    # ==========================================================
    # BEST MODEL
    # ==========================================================

    best_model = models[0]["model"]

    print("\n🏆 BEST MODEL")

    print("-" * 40)

    print(best_model)

    # ==========================================================
    # CREATE DIRECTORY
    # ==========================================================

    os.makedirs(

        "backend/saved_models",

        exist_ok=True

    )

    # ==========================================================
    # COPY BEST MODEL
    # ==========================================================

    if best_model == "Multi-Output Linear Regression":

        shutil.copy(

            "backend/saved_models/multi_linear_regression.pkl",

            "backend/saved_models/best_model.pkl"

        )

    elif best_model == "Multi-Output Random Forest":

        shutil.copy(

            "backend/saved_models/multi_random_forest.pkl",

            "backend/saved_models/best_model.pkl"

        )

    elif best_model == "Multi-Output XGBoost":

        shutil.copy(

            "backend/saved_models/multi_xgboost.pkl",

            "backend/saved_models/best_model.pkl"

        )

    else:

        raise ValueError(

            f"Unknown model: {best_model}"

        )

    print("\nBest model saved successfully!")

    print("Location:")

    print("backend/saved_models/best_model.pkl")

    print("\n")
    print("=" * 80)
    print("          MODEL COMPARISON COMPLETED SUCCESSFULLY")
    print("=" * 80)

    return best_model


if __name__ == "__main__":

    compare_models()