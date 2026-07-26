from picographics import PicoGraphics, DISPLAY_INKY_PACK


display = PicoGraphics(display=DISPLAY_INKY_PACK)


def clear():
    display.set_pen(15)
    display.clear()


def show_home():
    clear()

    display.set_pen(0)

    display.text(
        "BinBuddy",
        20,
        20,
        3
    )

    display.text(
        "Starting...",
        20,
        60,
        2
    )

    display.update()