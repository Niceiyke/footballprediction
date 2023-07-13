import os
import sys
from backend.exception import CustomException
from backend.logger import logging

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score

from backend.utils import save_obj


@dataclass
class ModelTrainerConfig:
    model=LogisticRegression()
    model_path= os.path.join('artifacts/models','model.pkl')
    os.makedirs('artifacts/models',exist_ok=True)
    
    

class ModelTrainer:
    def __init__(self) -> None:
        self.config=ModelTrainerConfig()

    def train_model(self,xtrain,ytrain,xtest,ytest):

        try:
            logging.info('data model training initiated')

            model=self.config.model.fit(xtrain,ytrain.values.ravel())

            logging.info('data model training completed')

            accuracy,precision=self.evaluate_model(model=model,x=xtest,y=ytest)

            if precision >65:
                save_obj(self.config.model_path,model)
                logging.info(f'data model object saving completed with a precision of {precision} and accuracy of {accuracy}')

            return model
        
        except Exception as e:
            raise CustomException(e,sys)


    def evaluate_model(self,model,x,y):
        try:
            logging.info('model evaluation initiated')
            prediction=model.predict(x)
            accuracy=round(accuracy_score(y_true=y,y_pred=prediction)*100,2)
            precision=round(precision_score(y_true=y,y_pred=prediction)*100,2)

            print(accuracy,precision)
            logging.info('model evaluation completed')

            return accuracy,precision
        
        except Exception as e:
            raise CustomException(e,sys)

        
