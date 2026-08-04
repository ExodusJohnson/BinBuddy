from wifi import connect_wifi
from clock import sync_time
from screens import show_screen
from buttons import check_buttons
import time


def refresh():

    connect_wifi()
    sync_time()
    show_screen()


# Initial startup
refresh()


while True:

    button = check_buttons()

    if button in ("A", "B", "C"):
        refresh()

    time.sleep(0.2)