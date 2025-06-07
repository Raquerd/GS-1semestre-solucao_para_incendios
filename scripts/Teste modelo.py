import pandas as pd, joblib, os, requests
from flask import Flask, request, jsonify
from datetime import datetime

path = "historico_incendios.xlsx"
app = Flask(__name__)

ml = joblib.load(r'C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\document\modelo_incendio.pkl') #<-Carregando modelo de Machine Learning

df = pd.DataFrame(
    {
    'TEMPERATURA':[35, 40, 32], 
    'HUMIDADE':[65, 49, 59], 
    'FUMACA':[34, 67, 43]
    }
)

pred = ml.predict(df)

df['RISCO'] = pred

print(df)
