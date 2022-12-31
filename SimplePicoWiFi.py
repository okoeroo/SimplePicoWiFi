import network
import utime as time


class SimplePicoWiFi():
    # Wait for connect success or failure
    # Max wait tries
    max_wait = 25

    def __init__(self, ssid, wifi_psk):
        # Check if wifi details have been set
        if len(ssid) == 0 or len(wifi_psk) == 0:
            raise RuntimeError('Please set wifi ssid and password in this script')

        self._ssid = ssid
        self._psk = wifi_psk

        self.wlan = None

    def disconnect(self):
        self.wlan.active(False)

    def connect(self):
        # Start connection
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.connect(self._ssid, self._psk)

        while self.max_wait > 0:
            # Check for failure or connected
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            self.max_wait -= 1
            print('waiting for connection...', self.wlan.status(), self.get_status())
            time.sleep_ms(400)

        # Handle connection error
        if self.wlan.status() != 3:
            raise RuntimeError('wifi connection failed %d' % self.wlan.status())

        print('status:', self.get_status())

    def get_status(self):
        """
        #define CYW43_LINK_DOWN (0)
        #define CYW43_LINK_JOIN (1)
        #define CYW43_LINK_NOIP (2)
        #define CYW43_LINK_UP (3)
        #define CYW43_LINK_FAIL (-1)
        #define CYW43_LINK_NONET (-2)
        #define CYW43_LINK_BADAUTH (-3)
        """
        status = self.wlan.status()
        if status == 0:
            return 'down'
        elif status == 1:
            return 'join'
        elif status == 2:
            return 'noip'
        elif status == 3:
            return 'up'
        elif status == -1:
            return 'fail'
        elif status == -2:
            return 'nonet'
        elif status == -3:
            return 'badauth'
        else:
            return 'unknown status'

    def get_ssid(self):
        return self._ssid

    def get_ip(self):
        if self.wlan.status() != 3:
            return None
        else:
            return self.wlan.ifconfig()[0]

    def get_subnet(self):
        if self.wlan.status() != 3:
            return None

        return self.wlan.ifconfig()[1]

    def get_gateway(self):
        if self.wlan.status() != 3:
            return None

        return self.wlan.ifconfig()[2]

    def get_dns(self):
        if self.wlan.status() != 3:
            return None

        return self.wlan.ifconfig()[3]

    def get_info_json(self) -> str:
        return "\n".join([ "\"wifi\": {",
                          f"    \"ssid\": \"{self.get_ssid()}\"",
                          f"    \"status\": \"{self.get_status()}\"",
                          f"    \"ip\": \"{self.get_ip()}\"",
                          f"    \"subnet\": \"{self.get_subnet()}\"",
                          f"    \"gateway\": \"{self.get_gateway()}\"",
                          f"    \"dns\": \"{self.get_dns()}\"",
                           "}"])

    def get_info(self) -> str:
        return ",".join([f"ssid:\"{self.get_ssid()}\"",
                         f"status:{self.get_status()}",
                         f"ip:{self.get_ip()}",
                         f"subnet:{self.get_subnet()}",
                         f"gateway:{self.get_gateway()}",
                         f"dns:{self.get_dns()}"])

    def __str__(self) -> str:
        return self.get_info()

    def __repr__(self) -> str:
        return f"SimplePicoWiFi({self.get_info()})"



if __name__ == "__main__":
    import urequests as requests
    import time

    from wifi import SimplePicoWiFi


    WIFI_SSID = const('example SSID')
    WIFI_PASSWORD = const('example WiFi password')

    wifi = SimplePicoWiFi(WIFI_SSID, WIFI_PASSWORD)
    wifi.connect()

    print(wifi.get_info())
    print(wifi)
    print(wifi.__repr__())
    print(wifi.get_info_json())

    res = requests.get(url='http://www.minvws.nl/')
    print(res.text)
