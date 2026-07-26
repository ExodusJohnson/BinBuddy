from display import display, clear
from config import COUNCIL
from bins import get_next_collection, format_bins
from utils import format_date
from weather import get_weather


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

        weather = get_weather()
        next_bin = get_next_collection()

        display.text(
            "BinBuddy",
            20,
            10,
            3
        )

        display.text(
            "NEXT BIN:",
            20,
            45,
            2
        )

        display.text(
            format_bins(next_bin["bins"]),
            20,
            70,
            2
        )

        display.text(
            format_date(next_bin["date"]),
            20,
            95,
            2
        )

        display.text(
            weather["temperature"],
            170,
            45,
            3
        )

        display.text(
            weather["condition"],
            150,
            80,
            2
        )


    elif screen == "bins":

        next_bin = get_next_collection()

        display.text(
            "NEXT BIN",
            20,
            20,
            3
        )

        display.text(
            format_bins(next_bin["bins"]),
            20,
            60,
            2
        )

        display.text(
            format_date(next_bin["date"]),
            20,
            100,
            2
        )


    elif screen == "weather":

        weather = get_weather()

        display.text(
            "WEATHER",
            20,
            20,
            3
        )

        display.text(
            weather["temperature"],
            20,
            60,
            3
        )

        display.text(
            weather["condition"],
            20,
            100,
            2
        )


    elif screen == "status":

        display.text(
            "STATUS",
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