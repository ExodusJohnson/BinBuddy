from display import display, clear


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
        display.text("BinBuddy", 20, 20, 3)
        display.text("Ready!", 20, 60, 2)

    elif screen == "bins":
        display.text("Bins", 20, 20, 3)
        display.text("Next collection", 20, 60, 2)

    elif screen == "weather":
        display.text("Weather", 20, 20, 3)
        display.text("Coming soon", 20, 60, 2)

    elif screen == "status":
        display.text("Status", 20, 20, 3)
        display.text("WiFi: OFF", 20, 60, 2)

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