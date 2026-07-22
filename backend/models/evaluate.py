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

    target_names = [
        "Open",
        "High",
        "Low",
        "Close"
    ]

    results = {}

    print("\n========================================")
    print(f"{model_name} RESULTS")
    print("========================================\n")

    maes = []
    mses = []
    rmses = []
    r2s = []
    mapes = []

    for i, target in enumerate(target_names):

        actual = y_true.iloc[:, i]
        predicted = predictions[:, i]

        mae = mean_absolute_error(actual, predicted)

        mse = mean_squared_error(actual, predicted)

        rmse = np.sqrt(mse)

        r2 = r2_score(actual, predicted)

        # Prevent division by zero
        mape = np.mean(
            np.abs(
                (actual - predicted) /
                np.where(actual == 0, 1, actual)
            )
        ) * 100

        maes.append(mae)
        mses.append(mse)
        rmses.append(rmse)
        r2s.append(r2)
        mapes.append(mape)

        print(f"---------- {target} ----------")
        print(f"MAE  : {mae:.4f}")
        print(f"MSE  : {mse:.4f}")
        print(f"RMSE : {rmse:.4f}")
        print(f"R²   : {r2:.4f}")
        print(f"MAPE : {mape:.2f}%")
        print()

        results[target.lower()] = {
            "mae": float(mae),
            "mse": float(mse),
            "rmse": float(rmse),
            "r2": float(r2),
            "mape": float(mape)
        }

    avg_mae = np.mean(maes)
    avg_mse = np.mean(mses)
    avg_rmse = np.mean(rmses)
    avg_r2 = np.mean(r2s)
    avg_mape = np.mean(mapes)

    print("========================================")
    print("AVERAGE PERFORMANCE")
    print("========================================")

    print(f"Average MAE  : {avg_mae:.4f}")
    print(f"Average MSE  : {avg_mse:.4f}")
    print(f"Average RMSE : {avg_rmse:.4f}")
    print(f"Average R²   : {avg_r2:.4f}")
    print(f"Average MAPE : {avg_mape:.2f}%")

    results["model"] = model_name

    results["mae"] = float(avg_mae)
    results["mse"] = float(avg_mse)
    results["rmse"] = float(avg_rmse)
    results["r2"] = float(avg_r2)
    results["mape"] = float(avg_mape)

    return results