import time

from wifi import connect_wifi
from clock import sync_time
from screens import show_screen


# ----------------------
# SETTINGS
# ----------------------

REFRESH_INTERVAL = 3600   # seconds (1 hour)


# ----------------------
# STARTUP
# ----------------------

print("BinBuddy starting")


connect_wifi()


sync_time()


# ----------------------
# MAIN LOOP
# ----------------------

while True:

    print("Updating display")

    show_screen()

    print("Display updated")

    print("Waiting 1 hour")


    time.sleep(
        REFRESH_INTERVAL
    )