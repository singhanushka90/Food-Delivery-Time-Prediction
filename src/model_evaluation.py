import os
import logging
import json
import joblib

from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("model_evaluation")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_file_path = os.path.join(log_dir,"model_evaluation.log")

file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)



def load_data(file_path):

    try:

        data = joblib.load(file_path)

        logger.debug("Data loaded successfully from %s",file_path)
        return data
    except Exception as e:
        logger.error("Error while loading data: %s",e)
        raise

def evaluate_model(model, X_test, y_test):

    try:

        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test,y_pred)
        mse = mean_squared_error(y_test,y_pred)
        rmse = mse ** 0.5
        r2 = r2_score(y_test,y_pred)
        metrics = {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "R2": r2
        }

        return metrics

    except Exception as e:

        logger.error("Error while evaluating model: %s",e)
        raise

def load_models():

    model_dir = "artifacts/model"

    model_files = {
        "Linear Regression": "linear_regression.pkl",
        "Decision Tree": "decision_tree.pkl",
        "Random Forest": "random_forest.pkl",
        "Gradient Boosting": "gradient_boosting.pkl",
        "XGBoost": "xgboost.pkl"
    }

    models = {}

    for name, file_name in model_files.items():

        file_path = os.path.join(model_dir,file_name)

        models[name] = load_data(file_path)

    logger.info("All models loaded successfully")

    return models


def save_metrics(metrics):

    evaluation_dir = "artifacts/evaluation"

    os.makedirs(evaluation_dir,exist_ok=True
    )

    metrics_path = os.path.join(evaluation_dir,"metrics.json")

    with open(metrics_path,"w") as file:

        json.dump(metrics,file,indent=4)

    logger.info("Metrics saved successfully at %s",metrics_path)



def save_final_model(model):

    model_dir = "artifacts/model"

    os.makedirs(model_dir,exist_ok=True)

    final_model_path = os.path.join(model_dir,"final_model.pkl"
    )

    joblib.dump(model,final_model_path)

    logger.info("Final model saved successfully at %s",final_model_path)


def main():

    try:
        X_test = load_data("artifacts/transformed/X_test.pkl")

        y_test = load_data("artifacts/transformed/y_test.pkl")
        models = load_models()
        all_metrics = {}

        for name, model in models.items():

            logger.info("Evaluating %s...",name)

            metrics = evaluate_model(
                model,
                X_test,
                y_test
            )

            all_metrics[name] = metrics

            logger.info(
                "%s → MAE: %.4f | MSE: %.4f | RMSE: %.4f | R2: %.4f",
                name,
                metrics["MAE"],
                metrics["MSE"],
                metrics["RMSE"],
                metrics["R2"]
            )

        best_model_name = min(
            all_metrics,key=lambda name: all_metrics[name]["RMSE"])

        best_model = models[best_model_name]

        logger.info(
            "Best model selected: %s",
            best_model_name
        )

        all_metrics["Best Model"] = best_model_name

        save_metrics(all_metrics)

        save_final_model(best_model)

        logger.info("Model evaluation pipeline completed successfully")

    except Exception as e:

        logger.error("Model evaluation pipeline failed: %s",e)

        raise


if __name__ == "__main__":
    main()