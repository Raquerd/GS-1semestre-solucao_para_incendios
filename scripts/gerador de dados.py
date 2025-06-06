import requests, json
import pandas as pd

latitude = -8.663648
longitude = -56.109233

start_date = "2024-06-02"
end_date = "2025-06-02"  # coloque o período desejado

url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={latitude}&longitude={longitude}"
    f"&start_date={start_date}&end_date={end_date}"
    f"&hourly=temperature_2m,precipitation,relative_humidity_2m,windspeed_10m"
    f"&timezone=America%2FSao_Paulo"
)

response = requests.get(url).json()
print(response)
df = pd.DataFrame(
    {
        'DATA':response['hourly']['time'], 
        'TEMPERATURA_MEDIA':response['hourly']['temperature_2m'], 
        'PRECIPITACAO':response['hourly']['precipitation'],
        'HUMIDADE':response['hourly']['relative_humidity_2m'], 
        'VENTOS':response['hourly']['windspeed_10m']
    }
)

df['DATA'] = pd.to_datetime(df['DATA'])

df.to_json(rf'C:\Users\Davi\Documents\Projetos\FIAP\FASE 4\Global Solutions\document\Dados_api_{start_date}_a_{end_date}.json')
print(df)