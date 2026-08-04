from picographics import PicoGraphics, DISPLAY_INKY_PACK


display = PicoGraphics(
    display=DISPLAY_INKY_PACK
)


inverted = False


def set_inverted(value):

    global inverted

    inverted = value



def get_background():

    if inverted:
        return 0

    return 15



def get_foreground():

    if inverted:
        return 15

    return 0



def clear():

    display.set_pen(
        get_background()
    )

    display.clear()