# 🔥 Sistema de Monitoramento e Previsão de Incêndios Florestais
Projeto completo de monitoramento ambiental utilizando ESP32, sensores físicos e um modelo de Machine Learning para prever o risco de incêndio em tempo real.

## Integrantes do projeto
**Davi Ferreira:** Códigos python administração do repostitório remoto (Github).

**Lais Kurahashi:** ESP32 + Diagrama.

**Lucas Martinelli:** Documentação.

## 📌 Índice
- 📖 Descrição do Projeto
- 🎯 Objetivos
- 🧠 Tecnologias Utilizadas
- 🔧 Arquitetura do Sistema
- 📡 Instalação e Execução
- 🧪 Exemplo de Uso
- 📂 Estrutura de Pastas
- 🤖 Sobre o Modelo de Machine Learning

## 📖 Descrição do Projeto
Incêndios florestais causam grandes danos ao meio ambiente e à sociedade, especialmente em regiões com clima seco e quente. A maioria das respostas ainda é reativa e tardia. Este projeto propõe uma solução de baixo custo que une sensores (ESP32) e inteligência artificial para monitorar o ambiente em tempo real, prever riscos de incêndio e enviar alertas automáticos. A aplicação visa antecipar ações de prevenção, proteger ecossistemas e oferecer uma ferramenta acessível e escalável para uso em áreas rurais, reservas e zonas de risco.

Esses dados são enviados via Wi-Fi para uma API Python, que:
- Classifica o risco de incêndio com base em um modelo de Machine Learning.
- Retorna o risco ao ESP32.
- Salva os dados e o resultado da classificação para uso posterior.
- Envia alertas automáticos em caso de risco alto.

## 🎯 Objetivos
🔍 Monitoraramento 24h do ambiente em tempo real com sensores físicos.

🧠 Aplicar Machine Learning para classificar o risco de incêndio.

🚨 Enviar alertas automáticos em caso de risco elevado.

💾 Armazenar os dados e previsões para histórico e análise futura.

## Tecnologias Utilizadas
- Backend (Python)
- Flask – Criação da API
- Scikit-learn – Treinamento do modelo
- Pandas – Manipulação de dados
- Joblib – Serialização do modelo
- Requests – Envio de alertas

## Hardware
- ESP32
- Sensor DHT11 ou DHT22 – Temperatura e umidade
- Sensor MQ-2/MQ-7 – Fumaça

## 🔧 Arquitetura do Sistema
```bash
[ESP32 + Sensores]
      ↓ Dados
[API Flask (Python)] 
      ↓
[Modelo ML .pkl] → Classificação
      ↓
[Resposta JSON + Armazenamento + Alerta Telegram]
```
## Instalação e Execução
1. Clone o projeto:
```bash
git clone https://github.com/seu-usuario/sistema-incendios.git
cd sistema-incendios
```

2. Instale as dependências Python:
```bash
pip install flask scikit-learn pandas joblib
```
3. Treine e salve o modelo:

```bash
python treinar_modelo.py
```
4. Inicie a API:
```bash
python api.py
```
5. Programe o ESP32 com o código Arduino:
Suba o código esp32_sensor.ino com as configurações de rede Wi-Fi e pinos do sensor.

Exemplo de Uso
JSON enviado pelo ESP32:
```bash
{
  "temperatura": 42,
  "umidade": 22,
  "fumaca": 600
}
```
Resposta da API:

```bash
{
  "risco": "Alto"
}
```
**Ação:**

Dados salvos no histórico.

Alerta enviado ao Telegram.

📂 Estrutura de Pastas
txt
``` bash
sistema-incendios/
│
├── api.py                   # API Flask principal
├── treinar_modelo.py        # Script para treinar e salvar o modelo
├── modelo_incendio.pkl      # Modelo treinado
├── salvar_dados.py          # Função para salvar os dados recebidos
├── alerta.py                # Função para enviar alerta via Telegram
├── dados_historico.csv      # Base com os dados armazenados
├── esp32_sensor.ino         # Código para ESP32 (Arduino)
└── README.md                # Este arquivo

```

## 🤖 Sobre o Modelo de Machine Learning
- Algoritmo: Random Forest

### Entradas do modelo:
- Temperatura
- Umidade
- Fumaça (gases)
- Saída: Classificação do risco: Baixo, Médio ou Alto
- Treinamento: Com dados simulados (pode ser adaptado para dados reais)
