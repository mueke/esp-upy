from config import *
import network

class Wifi:
    def do_connect(self, ssid, pwd):
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network '+ssid)
            wlan.connect(ssid,pwd)
            while not wlan.isconnected():
                pass
        print('network config:', wlan.ifconfig())

# TODO: Implement scan wifi method to choose the correct password from the config dict
Wifi().do_connect(WIFI_CREDS.keys()[0],WIFI_CREDS.values()[0])
