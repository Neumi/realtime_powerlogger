# realtime_powerlogger
An easy power logger for S0 interfaced power meters with internet connection and chart view.
Depending on the power meter you get data with 0.5Wh or 1Wh resolution in real-time on a website.


This setup can be used to log and preview solar power production data in real time. 

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
Upload the sketch to the NodeMCU.


<img src="/images/schematic.png" width="40%">

Connect the S0 device on P- from power meter to GPIO5/D1 and add a ~10k Ohm resistor between GPIO5/D1 and ground.
  
Connect 3.3V from ESP8266/NodeMCU to P+ on your S0 device.


# Check the website

Enter your servers IP address or domain name. When enough data is present, the page should show an overview with these two charts:

<img src="/images/real_time_solar_production.png" width="40%"> <img src="/images/solar_production.png" width="40%">


# Install the NodeMCU in a box near the power meter
<img src="/images/case_2.png" width="40%"> <img src="/images/installed.jpg" width="40%"> 
  
I added a Meanwell 5V power supply for DIN rails and used a DIN rail enclosure with three slots.
STL files for the NodeMCU for DIN rails are available in the STL folder.


## Video:
[![LINK TO VIDEO](https://img.youtube.com/vi/A4cKONG77xE/0.jpg)](https://www.youtube.com/watch?v=A4cKONG77xE)


## Disclaimer
Only people with training are allowed to work on power grids or mains voltage.
