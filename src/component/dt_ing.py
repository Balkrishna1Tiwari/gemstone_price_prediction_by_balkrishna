import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from exce import Custom_Exception
from logg import logging

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_class_ingestion(self):
        logging.info('Data ingestion method start')
        try:
            # Use default CSV path or provide fallback logic here
            csv_path = os.path.join('notebook/data', 'cubic_zirconia.csv')
            df = pd.read_csv(csv_path)
            logging.info('Dataset read as a pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info('Raw data is created')

            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')
            print("Hi")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path
        except Exception as e:
            logging.info('Exception occurred at data ingestion stage')
            raise Custom_Exception(str(e), sys)  # Pass str(e) instead of e, and remove error_details

# Assuming the Custom_Exception class and error_message_detail function are correctly defined in src.exception module

# x=DataIngestion()
# x.initiate_class_ingestion()
# kv

# hkjhkjhkjjkj