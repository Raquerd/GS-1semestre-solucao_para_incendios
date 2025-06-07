import requests, json
import pandas as pd, joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_excel(r"C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\document\base de treinamento.xlsx")
df.loc[df['FUMACA'] >= 0, 'RISCO'] = 'NENHUM RISCO'
df.loc[df['FUMACA'] >= 10, 'RISCO'] = 'BAIXO'
df.loc[df['FUMACA'] >= 21, 'RISCO'] = 'MEDIO'
df.loc[df['FUMACA'] >= 50, 'RISCO'] = 'ALTO'
df.loc[df['FUMACA'] >= 60, 'RISCO'] = 'ALERTA: INCENDIO'
print(df)

x = df[['TEMPERATURA', 'HUMIDADE', 'FUMACA']]
y = df['RISCO']

ml = RandomForestClassifier()
ml.fit(x, y)

joblib.dump(ml, r'C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\document\modelo_incendio.pkl')
