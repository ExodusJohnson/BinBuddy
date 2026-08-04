from picographics import PicoGraphics, DISPLAY_INKY_PACK

display = PicoGraphics(
    display=DISPLAY_INKY_PACK
)


def clear():
    display.set_pen(15)
    display.clear()
    display.update()