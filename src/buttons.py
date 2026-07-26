from machine import Pin


button_a = Pin(12, Pin.IN, Pin.PULL_UP)
button_b = Pin(13, Pin.IN, Pin.PULL_UP)
button_c = Pin(14, Pin.IN, Pin.PULL_UP)


def check_buttons():

    if not button_a.value():
        return "A"

    if not button_b.value():
        return "B"

    if not button_c.value():
        return "C"

    return None