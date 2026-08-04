from display import display


def draw_sun(x, y):

    display.circle(x, y, 12)

    display.line(x, y-20, x, y-14)
    display.line(x, y+14, x, y+20)
    display.line(x-20, y, x-14, y)
    display.line(x+14, y, x+20, y)



def draw_cloud(x, y):

    display.circle(x-10, y, 8)
    display.circle(x, y-6, 10)
    display.circle(x+12, y, 8)

    display.line(
        x-20,
        y+8,
        x+20,
        y+8
    )



def draw_rain(x, y):

    draw_cloud(x, y)

    display.line(x-10, y+15, x-10, y+25)
    display.line(x, y+15, x, y+25)
    display.line(x+10, y+15, x+10, y+25)



def draw_weather_icon(condition, x, y):

    condition = condition.lower()

    if "sun" in condition or "clear" in condition:
        draw_sun(x, y)

    elif (
        "rain" in condition
        or "shower" in condition
        or "drizzle" in condition
    ):
        draw_rain(x, y)

    elif "cloud" in condition:
        draw_cloud(x, y)

    else:
        draw_cloud(x, y)



def draw_bin(x, y):

    # small bin icon

    # handle
    display.line(
        x-3,
        y-10,
        x+3,
        y-10
    )

    # lid
    display.line(
        x-8,
        y-7,
        x+8,
        y-7
    )

    # body
    display.rectangle(
        x-8,
        y-5,
        16,
        22
    )

    # small front lines
    display.line(
        x-3,
        y-2,
        x-3,
        y+12
    )

    display.line(
        x+3,
        y-2,
        x+3,
        y+12
    )