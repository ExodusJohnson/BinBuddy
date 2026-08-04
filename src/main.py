import time

from wifi import connect_wifi
from clock import sync_time
from screens import show_screen
from buttons import check_buttons
from display import set_inverted, display, get_foreground


# ----------------------
# SETTINGS
# ----------------------

REFRESH_INTERVAL = 3600


inverted_mode = False



# ----------------------
# REFRESH FUNCTION
# ----------------------

def refresh_display():

    print("Refreshing")

    try:

        connect_wifi()

        sync_time()

        show_screen()

        print("Done")


    except Exception as e:

        print("Refresh failed:")
        print(e)



# ----------------------
# STARTUP
# ----------------------

refresh_display()



# ----------------------
# LOOP
# ----------------------

counter = 0


while True:

    time.sleep(1)

    counter += 1


    button = check_buttons()


    # Button A = refresh

    if button == "A":

        refresh_display()

        counter = 0



    # Button B = invert colours

    if button == "B":

        inverted_mode = not inverted_mode

        set_inverted(
            inverted_mode
        )

        refresh_display()

        counter = 0



    # Hourly refresh

    if counter >= REFRESH_INTERVAL:

        refresh_display()

        counter = 0