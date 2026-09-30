import os
import logging
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (RandomForestRegressor,GradientBoostingRegressor)
from xgboost import XGBRegressor



log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("model_trainer")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_file_path = os.path.join(log_dir, "model_trainer.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

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


def create_models():

    models = {

        "Linear Regression": LinearRegression(),

        "Decision Tree": DecisionTreeRegressor(random_state=42),

        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42
        ),

        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=2,
            min_samples_split=2,
            min_samples_leaf=2,
            random_state=42
        ),

        "XGBoost": XGBRegressor(
            n_estimators=100,
            learning_rate=0.05,
            max_depth=3,
            subsample=0.8,
            random_state=42,
            objective="reg:squarederror"
        )
    }

    logger.info("All models created successfully")

    return models


def train_models(models, X_train, y_train):

    trained_models = {}

    for name, model in models.items():

        try:
            logger.info("Training %s...",name)
            model.fit(X_train, y_train)
            trained_models[name] = model
            logger.info("%s trained successfully",name)
        except Exception as e:
            logger.error("Error while training %s: %s",name,e)
            raise
    return trained_models


def save_models(models):

    model_dir = "artifacts/model"
    os.makedirs(model_dir, exist_ok=True)
    for name, model in models.items():

        file_name = name.lower().replace(" ", "_") + ".pkl"

        file_path = os.path.join(model_dir,file_name)
        joblib.dump(model, file_path)

        logger.info("%s saved successfully at %s",name,file_path)


def main():

    try:
        X_train_path = ("artifacts/transformed/X_train.pkl")

        y_train_path = ("artifacts/transformed/y_train.pkl")
        X_train = load_data(X_train_path)
        y_train = load_data(y_train_path)

        models = create_models()

        trained_models = train_models(models,X_train,y_train)

        save_models(trained_models)

        logger.info("Model training pipeline completed successfully")
    except Exception as e:

        logger.error("Model training pipeline failed: %s",e)

        raise



if __name__ == "__main__":
    main()