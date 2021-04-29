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

Change baord settings to this:
  
<img src="/images/esp_settings.png" width="40%">
