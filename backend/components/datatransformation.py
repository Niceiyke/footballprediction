import os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from backend.pipeplines.fit_transform_model_pipeline import FitTransform
from backend.components.modelTrainer import ModelTrainer


@dataclass
class DataTransformationConfig:
    preprocessor=FitTransform()
    modeltrainer=ModelTrainer()
    preprocessor=preprocessor.fit_transform_data()
    train_data = os.path.join("artifacts", "train.csv")
    test_data = os.path.join("artifacts", "test.csv")
    predictors = [
        "hometeam",
        "awayteam",
        "b365h",
        "b365d",
        "b365a",
    ]
    target = ["target"]


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()
        self.labels= [
                "date",
                "hometeam",
                "awayteam",
                "b365h",
                "b365d",
                "b365a",
                "ftr",
            ]

    def process_data(self,train_df,test_df):
        train_df.columns = [dfc.lower() for dfc in train_df.columns]
        train_df = train_df[self.labels].copy()
        train_df["target"] = ((train_df["ftr"] == "H")).astype(int)
        train_df = train_df.dropna()

        test_df = pd.read_csv(self.config.test_data, low_memory=False)
        test_df.columns = [dfc.lower() for dfc in test_df.columns]
        test_df = test_df[self.labels].copy()
        test_df["target"] = ((test_df["ftr"] == "H")).astype(int)
        test_df = train_df.dropna()

        print('data processing done')
        
        self.transform_data(train=train_df,test=test_df)

        return train_df,test_df

    def transform_data(self,train,test):
        xtrain = train[self.config.predictors]
        ytrain = train[self.config.target]
        xtest = test[self.config.predictors]
        ytest = test[self.config.target]


        xtrain_df=self.config.preprocessor.fit_transform(xtrain)
        xtest_df=self.config.preprocessor.transform(xtest)
        

        xtrain_array = np.c_[xtrain_df, np.array(ytrain)]
        xtest_array = np.c_[xtest_df, np.array(ytest)]

        self.config.modeltrainer.train_model(xtrain=xtest_array,ytrain=ytrain,xtest=xtest_array,ytest=ytest)

        print('fitting done')

        return xtrain_array,xtest_array,ytrain,ytest

        
