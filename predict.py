import os
from backend.pipelines.prediction_pipeline import Predict


data_path = os.path.join("datasets", "test.csv")


def predict(data_path):
    obj = Predict(data=data_path,league='epl ')
    obj.make_prediction()


if __name__ == "__main__":
    predict(data_path=data_path)
