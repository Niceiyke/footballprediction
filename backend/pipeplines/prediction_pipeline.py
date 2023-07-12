import os
from dataclasses import dataclass
import pandas as pd
from backend.utils import load_obj
from backend.pipeplines.transform_pipeline import FitTransform



data_path=os.path.join('datasets','test.csv')

@dataclass
class PredictionPipelineConfig:
    preprocessor_path='artifacts\models\preprocessor.pkl'
    model_path='artifacts\models\model.pkl'
    preprocessor= load_obj(preprocessor_path)
    model= load_obj(model_path)
    obj=FitTransform()
    preprocessor=obj.fit_transform_data()



    
    

class Predict:
    def __init__(self,data) -> None:
        self.config =PredictionPipelineConfig()
        self.df= pd.read_csv(data,index_col=False)
        

    def make_prediction(self):


        X=self.config.preprocessor.transform(self.df)

        result=self.config.model.predict(X)

        return result
    
if __name__=='__main__':
    obj=Predict(data=data_path)
    obj.make_prediction()



        

        