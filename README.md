# SimplePicoWiFi
Simplified WiFi class for Pico for intuitive programming

## class SimplePicoWiFi
- init(ssid, wifi\_psk)
- disconnect()
- connect()
- get\_status() -> str
- get\_ssid() -> str
- get\_ip() -> str
- get\_subnet() -> str
- get\_gateway() -> str
- get\_dns() -> str
- get\_info\_json() -> str
- get\_info() -> str
- \_\_str\_\_() -> str
- \_\_repr\_\_() -> str


## Example
Load both this example or the `example.py` and the `SimplePicoWiFi.py` files on the Raspberry Pico-W to make it work.

```python
import urequests as requests
import time

from SimplePicoWiFi import SimplePicoWiFi

WIFI_SSID = const('example SSID')
WIFI_PASSWORD = const('example WiFi password')

wifi = SimplePicoWiFi(WIFI_SSID, WIFI_PASSWORD)
wifi.connect()

print(wifi.get_info())
print(wifi)
print(wifi.__repr__())
print(wifi.get_info_json())

res = requests.get(url='http://www.google.com/')
print(res.text)
```
