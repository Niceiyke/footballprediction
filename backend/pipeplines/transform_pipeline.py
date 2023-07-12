import os
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline




@dataclass
class FitTransformConfig:
    numerical_columns = ["b365h", "b365d", "b365a"]
    categorical_columns = ["hometeam", "awayteam"]
    processor_path= os.path.join('artifacts/models','preprocessor.pkl')
    os.makedirs('artifacts/models',exist_ok=True)



class FitTransform:
    def __init__(self) -> None:
        self.config = FitTransformConfig()

    def fit_transform_data(self):
        num_pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="mean")),
            ]
        )

        cat_pipeline = Pipeline(
            steps=[
                ("ordinal_encoder", OrdinalEncoder()),
            ]
        )

        preprocessor = ColumnTransformer(
            [
                ("num_pipeline", num_pipeline, self.config.numerical_columns),
                ("cat_pipelines", cat_pipeline, self.config.categorical_columns),
            ]
        )

        return preprocessor
