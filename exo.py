import network
import urequests
import time
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ssid = 'Sacha la tepu'
password= 'scarboule'
wlan.connect(ssid, password)
url= "http://192.168.43.151:3000/"

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
                
                print("gg")
        r.close()
        time.sleep(1)
    except Exception as e:
        print(e)