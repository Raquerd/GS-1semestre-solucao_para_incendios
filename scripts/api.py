import requests, json
import pandas as pd, joblib
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
ml = joblib.load(r"C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\document\da")

@app.route('/predict', methods =['POST'])
def predict():
    data = request.get_json() #<- Recebe os dados
    df = pd.Dataframe(data) #<- Transforma os dados em dataframe
    pred = ml.predict(df)[0] #<- Faz a prevenção dos dados com base no modelo machine learning disponibilizado
    return jsonify({'risco': pred}) #<- Envia a responsta da prevenção
