import requests, json
import pandas as pd, joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_excel(r"C:\Users\Davi\Downloads\download (2).xlsx")
df.loc[df['FUMACA'] >= 0, 'RISCO'] = 'sem riscos'
df.loc[df['FUMACA'] >= 10, 'RISCO'] = 'baixo'
df.loc[df['FUMACA'] >= 21, 'RISCO'] = 'medio'
df.loc[df['FUMACA'] >= 50, 'RISCO'] = 'alto'
df.loc[df['FUMACA'] >= 60, 'RISCO'] = 'muito alto'
print(df)

x = df[['TEMPERATURA', 'HUMIDADE', 'PRECIPITACAO', 'VENTOS', 'FUMACA']]
y = df['RISCO']

ml = RandomForestClassifier()
ml.fit(x, y)

joblib.dump(ml, r'C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\modelo_incendio.pkl')
