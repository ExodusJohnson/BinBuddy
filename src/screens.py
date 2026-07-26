from display import display, clear
from config import COUNCIL
from bins import get_next_collection, get_following_collection, format_bins
from utils import format_date


screens = [
    "home",
    "bins",
    "weather",
    "status"
]


current_screen = 0


def show_screen():

    clear()

    display.set_pen(0)

    screen = screens[current_screen]

    if screen == "home":

        display.text(
            "BinBuddy",
            20,
            20,
            3
        )

        display.text(
            "Ready!",
            20,
            60,
            2
        )


    elif screen == "bins":

        next_bin = get_next_collection()
        after_bin = get_following_collection()

        display.text(
            "NEXT BIN",
            20,
            15,
            3
        )

        display.text(
            format_bins(next_bin["bins"]),
            20,
            55,
            2
        )

        display.text(
            format_date(next_bin["date"]),
            20,
            85,
            2
        )


        display.text(
            "AFTER:",
            170,
            15,
            2
        )

        display.text(
            format_bins(after_bin["bins"]),
            170,
            55,
            2
        )


    elif screen == "weather":

        display.text(
            "Weather",
            20,
            20,
            3
        )

        display.text(
            "Coming soon",
            20,
            60,
            2
        )


    elif screen == "status":

        display.text(
            "Status",
            20,
            20,
            3
        )

        display.text(
            COUNCIL,
            20,
            60,
            2
        )


    display.update()



def next_screen():

    global current_screen

    current_screen += 1

    if current_screen >= len(screens):
        current_screen = 0



def previous_screen():

    global current_screen

    current_screen -= 1

    if current_screen < 0:
        current_screen = len(screens) - 1