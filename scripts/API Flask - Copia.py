import pandas as pd, joblib, os
from flask import Flask, request, jsonify
from datetime import datetime

path = "historico_incendios.xlsx"
app = Flask(__name__)

ml = joblib.load(r'C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\document\modelo_incendio.pkl') #<-Carregando modelo de Machine Learning


def salvar_dados(dados, risco):
    df = pd.DataFrame([dados]) #<-Criando dataframe
    df['risco'] = risco #<-nomeando coluna risco
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #<- Definindo coluna de data

    if os.path.exists(path): #<- Verifica se o arquivo excel existe
        existente = pd.read_excel(path) #<-Caso exista, abre o arquivo
        df_final = pd.concat([existente, df], ignore_index=True) #<-Concatena as novas informações no arquivo existente
    else:
        df_final = df

    df_final.to_excel(path, index=False) #<- Salva o arquivo

@app.route('/predict', methods =['POST'])
def predict():
    data = request.get_json() #<- Recebe os dados
    df = pd.Dataframe(data) #<- Transforma os dados em dataframe
    pred = ml.predict(df)[0] #<- Faz a prevenção dos dados com base no modelo machine learning disponibilizado
    return jsonify({'risco': pred}) #<- Envia a responsta da prevenção
    salvar_dados(df, pred) #<- Salva os dados

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

