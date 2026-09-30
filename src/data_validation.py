import pandas as pd
import logging
import os

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)

logger=logging.getLogger("data_validation")
logger.setLevel("DEBUG")

console_handler=logging.StreamHandler()
console_handler.setLevel("DEBUG")

log_file_path=os.path.join(log_dir,'data_validation.log')
file_handler=logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_data(file_path:str):
    "Load data from the file"
    try:
        df=pd.read_csv(file_path)
        logger.debug("Data loaded from: %s",file_path)
        return df
    except Exception as e:
        logger.error("Error while loading file : %s",e)
        raise

    
def validate_column(df:pd.DataFrame):
    expected_columns=[
        "Order_ID",
        "Distance_km",
        "Weather",
        "Traffic_Level",
        "Time_of_Day",
        "Vehicle_Type",
        "Preparation_Time_min",
        "Courier_Experience_yrs",
        "Delivery_Time_min"
    ]
    missing_column=[column for column in expected_columns
                    if column not in df.columns]
    if missing_column:
        logger.error("Missing columns: %s",missing_column)
        return False
    logger.debug("All required re present.")
    return True


def validate_missing(df:pd.DataFrame):
    missing=df.isnull().sum()
    if missing.sum()>0:
        logger.warning("Missing values found")
        logger.warning("\n%s",missing[missing>0])
    else:
        logger.debug("No missing values found")
    return True

def validate_target(df:pd.DataFrame):
    target="Delivery_Time_min"
    if target not in df.columns:
        logger.error("Target column % s is missing",target)
        return False
    if df[target].isnull().any():
        logger.error("Target column contains missing values")
        return False
    logger.debug("Target column validation successfully")
    return True

def main():
    try:
        file_path="artifacts/raw/Food_Delivery_Times.csv"
        df=pd.read_csv(file_path)
        logger.debug("First five rows :\n%s",df.head())
        columns_valid=validate_column(df)
        columns_missing=validate_missing(df)
        columns_target=validate_target(df)
        if all ([
            columns_valid,
            columns_missing,
            columns_target
        ]):

            logger.info("Data validation completed Successfully")
        else:
            logger.error("Data validation failed")
    except Exception as e:
        logger.error("Error during data validation: %s",e)
        raise

if __name__=="__main__":
    main()

    