import pandas as pd
import pickle
from sqlalchemy import create_engine



def transformCSV():
    df=pd.read_csv('/home/niceiyke/Documents/WORK_FOLDER/footballprediction/datasets/test.csv')
    test_df=df.copy()
    test_df.dropna(inplace=True)
    predictors=['home_code','away_code','b365h','b365d','b365a']
    df=test_df[predictors]
    return predict(df)


def predict(df):
    model = pickle.load(open('/home/niceiyke/Documents/WORK_FOLDER/footballprediction/datasets/epl_model.pkl', 'rb'))
    pred=model.predict(df)
    df.insert(5,'predictions',pred)
    saveToDB(df)
    return df


def saveToDB(data):
    engine=create_engine('sqlite:///data.db')
    data.to_sql('predictions',engine,if_exists='replace', index=False)
    print('done')
