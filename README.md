# realtime_powerlogger
An easy power logger for S0 interfaced power meters with internet connection and chart view.


# Instalation Server
```sudo apt install nohub ```
  
```git clone https://github.com/Neumi/realtime_powerlogger ```

```cd realtime_powerlogger```

``` nohup python3 receive.py &```

``` nohup python3 serve.py &```

Ports 5005 for UDP and 80 for TCP have to be open to public.

When both scripts are running you can enter the servers IP or domain name in a Browser to access the website.

# Installation Arduino ESP8266
Add ```https://arduino.esp8266.com/stable/package_esp8266com_index.json``` to Arduinos 'Additional Boards Manager URL'

Change board settings to this:
  
<img src="/images/esp_settings.png" width="40%">

Change network and server settings:
```cpp 
const char *ssid = "NETWORK_NAME"; //CHANGE HERE WIFI NETWORK NAME
const char *password = "NETWORK_PASSWORD"; //CHANGE HERE WIFI PASSWORD
#define serverIp "111.222.333.444" //CHANGE HERE TO SERVER IP
```
Upload Sketch to NodeMCU.
Connect S0 output from power meter to GPIO5/D1 and add a ~10k Ohm resistor to GPIO5/D1 and ground.
Connect 3.3V from ESP8266/NodeMCU to P+ of your S0 device.

