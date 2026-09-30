import pandas as pd
import logging
import os
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from joblib import dump


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("data_transformation")
logger.setLevel("DEBUG")

console_handler = logging.StreamHandler()
console_handler.setLevel("DEBUG")

log_file_path = os.path.join(log_dir, "data_transformation.log")
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)




def load_data(file_path: str):

    try:
        df = pd.read_csv(file_path)
        logger.debug("Data loaded from the csv file: %s", file_path)
        return df

    except Exception as e:
        logger.error("Error while loading file: %s", e)
        raise



def remove(df: pd.DataFrame):

    try:
        df = df.drop(columns=["Order_ID"])
        logger.debug("Order_ID removed successfully")
        return df

    except Exception as e:
        logger.error("Error while removing Order_ID: %s", e)
        raise


def split_data(df: pd.DataFrame):

    try:
        X = df.drop(columns=["Delivery_Time_min"])
        y = df["Delivery_Time_min"]
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        logger.debug("Train-test split completed successfully")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logger.error("Error during train-test split: %s", e)
        raise



def create_preprocessor():

    numerical_cols = [
        "Distance_km",
        "Preparation_Time_min",
        "Courier_Experience_yrs"
    ]

    categorical_cols = [
        "Weather",
        "Traffic_Level",
        "Time_of_Day",
        "Vehicle_Type"
    ]

    numerical_pipeline = Pipeline([("imputer", SimpleImputer(strategy="median"))])

    categorical_pipeline = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),("encoder", OneHotEncoder(handle_unknown="ignore"))])

    preprocessor = ColumnTransformer([("num", numerical_pipeline, numerical_cols),("cat", categorical_pipeline, categorical_cols)])

    logger.debug("Preprocessor created successfully")

    return preprocessor


def transform_data(X_train, X_test, preprocessor):

    try:
        X_train_pro = preprocessor.fit_transform(X_train)
        X_test_pro = preprocessor.transform(X_test)
        logger.debug("Data transformation completed successfully")
        return X_train_pro, X_test_pro

    except Exception as e:
        logger.error("Error during data transformation: %s", e)
        raise



def save_data(data, file_path):

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        dump(data, file_path)
        logger.debug("Data saved successfully at %s", file_path)
    except Exception as e:
        logger.error("Error while saving data: %s", e)
        raise




def main():

    try:

        file_path = "artifacts/raw/Food_Delivery_Times.csv"

        df = load_data(file_path)

        df = remove(df)

        X_train, X_test, y_train, y_test = split_data(df)

        preprocessor = create_preprocessor()

        X_train_pro, X_test_pro = transform_data(X_train,X_test,preprocessor)

        os.makedirs("artifacts/transformed", exist_ok=True)

        save_data(X_train_pro,"artifacts/transformed/X_train.pkl")

        save_data(X_test_pro,"artifacts/transformed/X_test.pkl")

        save_data(y_train,"artifacts/transformed/y_train.pkl")

        save_data(y_test,"artifacts/transformed/y_test.pkl")

        save_data(preprocessor,"artifacts/transformed/preprocessor.pkl")

        logger.info("Data transformation pipeline completed successfully")

    except Exception as e:

        logger.error("Error in data transformation pipeline: %s",e)

        raise


if __name__ == "__main__":
    main()

              
    