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
