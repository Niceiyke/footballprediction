import os
import sys
from backend.exception import CustomException
from dataclasses import dataclass
import pandas as pd
from backend.utils import load_obj





data_path=os.path.join('datasets','test.csv')

@dataclass
class PredictionPipelineConfig:

    predictors = [
        "hometeam",
        "awayteam",
        "b365h",
        "b365d",
        "b365a",
    ]


class Predict:
    def __init__(self,data,league) -> None:
        self.league=league
        self.config =PredictionPipelineConfig()
        self.df= pd.read_csv(data,index_col=False)
        preprocessor_path=os.path.join('artifacts/models',f'{self.league}_preprocessor.pkl')
        model_path=os.path.join('artifacts/models',f'{self.league}_model.pkl')
        self.preprocessor= load_obj(preprocessor_path)
        self.model= load_obj(model_path)
        

    def make_prediction(self):

        try:
            df=self.df[self.config.predictors]

            X=self.preprocessor.fit_transform(df)

            pred=self.config.model.predict(X)
            prob=self.config.model.predict_proba(X)
            prob=(prob[:,1])
            prob=[round(p*100,0) for p in prob]
            hodd=[round((1/p)*100,2) for p in prob]
            aprob=[(100-p) for p in prob]
            aodd=[round((1/p)*100,2) for p in aprob]

            self.df.insert(5,'Home Prob',prob)
            self.df.insert(6,'Away prob',aprob)
            self.df.insert(7,'Home Odd',hodd)
            self.df.insert(8,'Away Odd',aodd)
            self.df.insert(9,'predictions',pred)

            print(self.df.head(30))

            return pred
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__=='__main__':
    obj=Predict(data=data_path,league='epl ')
    obj.make_prediction()



        

        