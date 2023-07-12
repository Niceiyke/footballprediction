import os
from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score

from backend.utils import save_obj


@dataclass
class ModelTrainerConfig:
    model=LogisticRegression(C=7,solver='liblinear')
    model_path= os.path.join('artifacts/models','model.pkl')
    os.makedirs('artifacts/models',exist_ok=True)
    
    

class ModelTrainer:
    def __init__(self) -> None:
        self.config=ModelTrainerConfig()

    def train_model(self,xtrain,ytrain,xtest,ytest):

        model=self.config.model.fit(xtrain,ytrain.values.ravel())



        _,precision=self.evaluate_model(model=model,x=xtest,y=ytest)

        if precision >80:
            save_obj(self.config.model_path,model)

        print('training done')

        return model


    def evaluate_model(self,model,x,y):
        prediction=model.predict(x)
        accuracy=accuracy_score(y_true=y,y_pred=prediction)*100
        precision=precision_score(y_true=y,y_pred=prediction)*100

        print('evaluation done')


        print(accuracy,precision)
        

        return accuracy,precision

        
