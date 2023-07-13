import os
import sys
from backend.exception import CustomException
from dataclasses import dataclass
import pandas as pd
from backend.utils import load_obj





data_path=os.path.join('datasets','test.csv')

@dataclass
class PredictionPipelineConfig:
    preprocessor_path=os.path.join('artifacts/models','preprocessor.pkl')
    model_path=os.path.join('artifacts/models','model.pkl')
    preprocessor= load_obj(preprocessor_path)
    model= load_obj(model_path)
    predictors = [
        "hometeam",
        "awayteam",
        "b365h",
        "b365d",
        "b365a",
    ]



    
    

class Predict:
    def __init__(self,data) -> None:
        self.config =PredictionPipelineConfig()
        self.df= pd.read_csv(data,index_col=False)
        

    def make_prediction(self):

        try:
            df=self.df[self.config.predictors]

            X=self.config.preprocessor.fit_transform(df)

            pred=self.config.model.predict(X)

            self.df.insert(5,'predictions',pred)

            print(self.df.head())

            return pred
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__=='__main__':
    obj=Predict(data=data_path)
    obj.make_prediction()



        

        