import os
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
        print("started")

        df = pd.read_csv(
            "datasets/epl.csv",
            low_memory=False,
        )

        df["date"] = pd.to_datetime(df["date"], format="mixed", dayfirst=True)

        train = df[df["date"] < "2022-09-01"]
        test = df[df["date"] > "2022-09-01"]

        train.to_csv(self.config.train_data_path, index=False, header=True)
        test.to_csv(self.config.test_data_path, index=False, header=True)

        print('dataingestation done')

        self.config.data_transform.process_data(train_df=train, test_df=test)

        print("done")


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
