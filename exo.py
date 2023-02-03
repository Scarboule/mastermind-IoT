import network
import urequests
import time
import ujson
from machine import Pin
import _thread

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = 'Sacha la tepu'
password= 'scarboule'
wlan.connect(ssid, password)
url= "http://192.168.43.109:3000/"


all_led = [Pin(17, mode=Pin.OUT),Pin(18, mode=Pin.OUT),Pin(20, mode=Pin.OUT),Pin(22, mode=Pin.OUT)]
btn = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)


while not wlan.isconnected():
    time.sleep(1)
    print("noco")

while(True):
    print(url + "reset/")
    print(btn.value())
    if btn.value() == 1:
        r = urequests.get(url + "reset")
        result = r.json()
        print(result)
    time.sleep(0.1)
    try:
        for i in range(len(all_led)):
            all_led[i].off()
        r = urequests.get(url)
        result = r.json()
        print(result)
        for i in range(len(result['chosencolor'])):
            if result['chosencolor'][i] == result['resultcolor'][i]:
                all_led[i].on()
            
        r.close()
        time.sleep(0.5)
    except Exception as e:
        print(e)