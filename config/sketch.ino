#include <DHT.h> // Biblioteca para o sensor de umidade DHT22
#include <WiFi.h>
#include <HTTPClient.h>

#define DHTPIN 0
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

int sensor_fumaca = 4;

const char* ssid = "nome da rede";
const char* password = "senha da rede";
const char* servername = "http://127.0.0.1:5000"; //Ip inserido foi gerado pelo flask no python


void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    float temperatura = dht.readTemperature();
    float umidade = dht.readHumidity();
    int fumaca = analogRead(sensor_fumaca);

    HTTPClient  http;
    http.begin(servername);
    http.addHeader("Content-Type", "application/json");

    if (isnan(umidade)) {
      Serial.println("Erro: leitura inválida do DHT22. Usando valor padrão de 50%.");
      umidade = 50.0;  // Valor fictício para manter o funcionamento
    }
    if (isnan(temperatura)) {
      Serial.println("Erro: Leitura inválida do DHT22. Usando temperatura média");
      temperatura = 28.5;
    }

    String jsonData = "{\"temperatura\": " + String(temperatura, 1) +
                      ", \"umidade\": " + String(umidade, 1) +
                      ", \"fumaca\": " + String(fumaca) + "}";

    int httpResponseCode = http.POST(jsonData);
    String resposta = http.getString();

    http.end();
  }

  delay(60000);
}

