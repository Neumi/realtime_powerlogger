#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

const char *ssid = "NETWORK_NAME"; //CHANGE HERE WIFI NETWORK NAME
const char *password = "NETWORK_PASSWORD"; //CHANGE HERE WIFI PASSWORD

#define serverIp "111.222.333.444" //CHANGE HERE TO SERVER IP
#define deviceId 1

WiFiUDP Udp;
unsigned int localUdpPort = 5005;

int last_input_value = 0;
int input_value = 0;
int input_pin = 5;
int last_spike = 0;
int time_since_last_spike = 0;


void setup()
{
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

}

void loop()
{
  input_value = digitalRead(input_pin);
  // Serial.println(input_value);
  if (input_value && !last_input_value) {
    time_since_last_spike = millis() - last_spike;
    String content = "{\"device\":";
    content += String(deviceId);
    content += ", \"last_ping\":";
    content += String(time_since_last_spike);
    content += "}";
    // Serial.println(content);
    sendUDP(content);
    last_spike = millis();
  }

  delay(10);
  last_input_value = input_value;
}

void sendUDP(String content) {
  Udp.begin(localUdpPort);
  Udp.beginPacket(serverIp, localUdpPort);
  Udp.print(content);
  Udp.endPacket();
}
