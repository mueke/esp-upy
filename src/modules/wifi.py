from config import *
import network

class Wifi:
    '''
    Connects to the Wifi defined in config.py
    Could have multiple ssid configured
    '''
    def __init__(self,config_dict):
        self.config_dict = config_dict
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        
    def get_ssid_list_sorted(self):
        'Strongest wifi first'
        self.ssid_list = list(map(lambda x: [x[0].decode(),x[3]], self.wlan.scan()) )
        self.ssid_list.sort(key=lambda y:y[1],reverse=True)
        return self.ssid_list
        
    def do_connect(self,force=False):
        
        try:
            if self.wlan.isconnected() and not force:
                return True
            for ssid_pair in self.get_ssid_list_sorted():
                ssid = ssid_pair[0]
                pwd = WIFI_CREDS.get(ssid,None)
                if pwd is None:
                    continue
                print("Trying to connect to ",ssid)
                if not self.wlan.isconnected() or force:
                    print('connecting to network '+ssid)
                    self.wlan.connect(ssid,pwd)
                    while not self.wlan.isconnected():
                        pass
                    if force:
                        force=False
                    print("connected")
        except:
            print('Problem connecting to wifi. Tried: ',WIFI_CREDS.keys())
            return False
        finally:
            print('network config:', self.wlan.ifconfig())
        
        

Wifi(WIFI_CREDS).do_connect()
