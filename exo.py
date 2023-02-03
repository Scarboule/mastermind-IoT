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

red_btn = Pin(10, mode=Pin.IN, pull=Pin.PULL_UP)
blue_btn = Pin(11, mode=Pin.IN, pull=Pin.PULL_UP)
green_btn = Pin(12, mode=Pin.IN, pull=Pin.PULL_UP)
yellow_btn = Pin(13, mode=Pin.IN, pull=Pin.PULL_UP)

all_led = [Pin(17, mode=Pin.OUT),Pin(18, mode=Pin.OUT),Pin(20, mode=Pin.OUT),Pin(22, mode=Pin.OUT)]
btn_reset = Pin(15, mode=Pin.IN, pull=Pin.PULL_UP)
color_btn = [
    red_btn,
    blue_btn,
    green_btn,
    yellow_btn
]
choosen_color = []

def selecColors():
    print("choose new color")
    while len(choosen_color) < 4:
        if btn_reset.value() == 0:
            r = urequests.get('http://192.168.43.109:3000/reset')
            print(r.json())
            r.close()
            print("reset")
            for i in range(len(all_led)):
                all_led[i].off()
        
        x = 0
        for i in color_btn: 
            if i.value() == 0:
                choosen_color.append(x)
                print(choosen_color)
            x += 1
        time.sleep(0.15)
    r = urequests.post('http://192.168.43.109:3000/choosecolor', json = 
    {
        'color1' : choosen_color[0],
        'color2' : choosen_color[1],
        'color3' : choosen_color[2],
        'color4' : choosen_color[3]
    })
    r.close()



while not wlan.isconnected():
    time.sleep(1)
    print("noco")

def resetcolor():
    r = urequests.post('http://192.168.43.109:3000/resetchoosecolor')
    r.close()


while True:
    selecColors()
    choosen_color = []

    

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
        resetcolor()
        time.sleep(2)
    except Exception as e:
        print(e)


