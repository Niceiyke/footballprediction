from flask import Flask,render_template,request
import pandas as pd
from backend.pipelines.csvTransformer import transformCSV

app =Flask(__name__)





@app.route("/predict",methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        file=request.files['file']
        df=pd.read_csv(file)
        data=transformCSV()
   
    return render_template('index.html')