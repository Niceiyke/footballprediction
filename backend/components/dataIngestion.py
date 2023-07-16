import os
import sys
from backend.exception import CustomException
from backend.logger import logging
import pandas as pd
from dataclasses import dataclass
from backend.components.datatransformation import DataTransformation


@dataclass
class DataIngestionConfig:
    data_transform = DataTransformation()
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")
    os.makedirs("artifacts", exist_ok=True)


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
       
       try:
            logging.info('dataingestion initiated')

            df = pd.read_csv(
                "datasets/epl .csv",
                low_memory=False,
            )

            df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)
            df.sort_values(by='date',ascending=True,inplace=True)

            train = df[df["date"] < "2022-09-01"]
            test = df[df["date"] > "2022-09-01"]

            train.to_csv(self.config.train_data_path, index=False, header=True)
            test.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info('dataingestion completed')

            self.config.data_transform.process_data(train_df=train, test_df=test)

            return train,test
       
       except Exception as e:
           raise CustomException(e,sys)


