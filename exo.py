import network
import urequests
import time
import ujson
from machine import Pin

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = 'Sacha la tepu'
password= 'scarboule'
wlan.connect(ssid, password)
url= "http://192.168.43.151:3000/"


all_led = [Pin(17, mode=Pin.OUT),Pin(18, mode=Pin.OUT),Pin(20, mode=Pin.OUT),Pin(22, mode=Pin.OUT)]
for i in range (len(all_led)):
    all_led[i].off()

while not wlan.isconnected():
    time.sleep(1)
    print("noco")

while(True):
    try:
        r = urequests.get(url)
        result = r.json()
        print(result)
        for i in range(len(result['chosencolor'])):
            if result['chosencolor'][i] == result['resultcolor'][i]:
                all_led[i].on()
            
        r.close()
        time.sleep(1)
    except Exception as e:
        print(e)