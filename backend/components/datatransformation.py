import os
import sys
from backend.exception import CustomException
from backend.logger import logging
from dataclasses import dataclass
import pandas as pd
import numpy as np
from backend.pipelines.transform_pipeline import FitTransform
from backend.components.modelTrainer import ModelTrainer


@dataclass
class DataTransformationConfig:
    preprocessor = FitTransform()
    preprocessor = preprocessor.fit_transform_data()

    modeltrainer = ModelTrainer()
    train_data = os.path.join("artifacts", "train.csv")
    test_data = os.path.join("artifacts", "test.csv")
    predictors = [
        "hometeam",
        "awayteam",
        "b365h",
        "b365d",
        "b365a",
        'b365>2.5','b365<2.5'
    ]
    target = ["target"]


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()
        self.labels = [
            "hometeam",
            "awayteam",
            "b365h",
            "b365d",
            "b365a",
            'b365>2.5','b365<2.5',
            "ftr",
        ]

    def process_data(self, train_df, test_df):
        try:
            logging.info('preprocessing of data initiated')
            train_df = pd.read_csv(self.config.train_data, low_memory=False)
            train_df.columns = [dfc.lower() for dfc in train_df.columns]
            train_df = train_df[self.labels].copy()
            train_df["target"] = ((train_df["ftr"] == "H")).astype(int)
            train_df = train_df.dropna()

            test_df = pd.read_csv(self.config.test_data, low_memory=False)
            test_df.columns = [dfc.lower() for dfc in test_df.columns]
            test_df = test_df[self.labels].copy()
            test_df["target"] = ((test_df["ftr"] == "H")).astype(int)
            test_df = train_df.dropna()

            logging.info('preprocessing of data completed')

            self.transform_data(train=train_df, test=test_df)

            return train_df, test_df
        except Exception as e:
            raise CustomException(e, sys)

    def transform_data(self, train, test):
       
       try:
            logging.info('data transform initiated')
            xtrain = train[self.config.predictors]
            ytrain = train[self.config.target]
            xtest = test[self.config.predictors]
            ytest = test[self.config.target]

            xtrain_df = self.config.preprocessor.fit_transform(xtrain)
            xtest_df = self.config.preprocessor.transform(xtest)
            logging.info('data transform completed')

            self.config.modeltrainer.train_model(
                xtrain=xtrain_df, ytrain=ytrain, xtest=xtest_df, ytest=ytest
            )

            print("fitting done")
            return xtrain_df, xtest_df, ytrain, ytest
       
       except Exception as e:
           raise CustomException(e,sys)
