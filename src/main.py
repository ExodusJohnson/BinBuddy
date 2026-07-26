from wifi import connect_wifi
from clock import sync_time
from screens import show_screen, next_screen, previous_screen
from buttons import check_buttons
import time


connect_wifi()

sync_time()

show_screen()


while True:

    button = check_buttons()

    if button == "A":
        previous_screen()
        show_screen()

    elif button == "C":
        next_screen()
        show_screen()

    elif button == "B":
        show_screen()

    time.sleep(0.2)