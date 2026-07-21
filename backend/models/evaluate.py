import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_model(
    y_true,
    predictions,
    model_name
):

    mae = mean_absolute_error(
        y_true,
        predictions
    )

    mse = mean_squared_error(
        y_true,
        predictions
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_true,
        predictions
    )

    mape = np.mean(
        np.abs(
            (y_true - predictions) / y_true
        )
    ) * 100

    print("\n========================================")
    print(f"{model_name} RESULTS")
    print("========================================\n")

    print(f"MAE  : {mae:.4f}")
    print(f"MSE  : {mse:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R²   : {r2:.4f}")
    print(f"MAPE : {mape:.2f}%")

    return {

    "model": model_name,

    "mae": float(mae),

    "mse": float(mse),

    "rmse": float(rmse),

    "r2": float(r2),

    "mape": float(mape)

}