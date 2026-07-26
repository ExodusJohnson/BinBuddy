import network
import time
from secrets import WIFI_SSID, WIFI_PASSWORD


def connect_wifi():

    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    print("WiFi active")

    print("Connecting to:")
    print(WIFI_SSID)

    wlan.connect(
        WIFI_SSID,
        WIFI_PASSWORD
    )

    timeout = 30

    while not wlan.isconnected() and timeout > 0:

        print("Waiting...", timeout)

        time.sleep(1)

        timeout -= 1


    if wlan.isconnected():

        print("Connected!")
        print(wlan.ifconfig())

        return True

    else:

        print("Connection failed")
        print("Status:")
        print(wlan.status())

        return False