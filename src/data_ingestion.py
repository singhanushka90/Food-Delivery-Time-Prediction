import pandas as pd
import os
import logging

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)

logger=logging.getLogger("data_ingestion")
logger.setLevel("DEBUG")

console_handler=logging.StreamHandler()
console_handler.setLevel("DEBUG")

log_file_path=os.path.join(log_dir,"data_ingestion.log")
file_handler=logging.FileHandler(log_file_path)
file_handler.setLevel("DEBUG")

formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def load_data(data_url:str)->pd.DataFrame:
    "Load data form a csv file"
    try:
        df=pd.read_csv(data_url)
        logger.debug("Data loaded from %s",data_url)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the CSV file: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error occurred while loading the data: %s', e)
        raise


def save_data(df:pd.DataFrame,file_path:str):
    "Save the data"
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        df.to_csv(file_path,index=False)
        logger.debug("Data Saved at %s",file_path)
    except Exception as e:
        logger.error("Unexpected error while saving the data : %s",e)
        raise

        

def main():
    try:
        data_path='experiments/Food_Delivery_Times.csv'
        df=load_data(data_url=data_path)
        save_path="artifacts/raw/Food_Delivery_Times.csv"
        save_data(df,save_path)
    except Exception as e:
        logger.error("Error in the data ingestion: %s",e)
        raise

if __name__=="__main__":
    main()


    


    


