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

red_btn = Pin(10, mode=Pin.IN),
blue_btn = Pin(11, mode=Pin.IN),
green_btn = Pin(12, mode=Pin.IN),
yellow_btn = Pin(13, mode=Pin.IN)

all_led = [Pin(17, mode=Pin.OUT),Pin(18, mode=Pin.OUT),Pin(20, mode=Pin.OUT),Pin(22, mode=Pin.OUT)]
btn_reset = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)
color_btn = [
    red_btn,
    blue_btn,
    green_btn,
    yellow_btn
]


while not wlan.isconnected():
    time.sleep(1)
    print("noco")



while True:
    if btn_reset.value() == 0:
        r = urequests.get('http://192.168.43.109:3000/reset')
        print(r.json())
        r.close()
        print("press")
    print("null")

    try:
        for i in range(len(all_led)):
            all_led[i].off()
        print("request get")
        r = urequests.get(url)
        result = r.json()
        print(result)
        for i in range(len(result['chosencolor'])):
            if result['chosencolor'][i] == result['resultcolor'][i]:
                all_led[i].on()
            
        r.close()
        time.sleep(2)
    except Exception as e:
        print(e)


