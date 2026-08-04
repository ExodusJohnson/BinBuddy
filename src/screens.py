from display import display, clear, get_foreground
from bins import get_next_collection, format_bins
from utils import format_date, days_until
from weather import get_weather
from icons import draw_weather_icon


def show_screen():

    clear()

    display.set_pen(
        get_foreground()
    )

    weather = get_weather()

    next_bin = get_next_collection()


    bin_name = format_bins(
        next_bin["bins"]
    ).upper()


    date = format_date(
        next_bin["date"]
    )


    days = days_until(
        next_bin["date"]
    ).upper()


    temperature = weather.get(
        "temperature",
        ""
    )


    condition = weather.get(
        "condition",
        ""
    ).upper()


    rain = weather.get(
        "rain",
        ""
    )


    # HEADER

    display.text(
        "NEXT BIN",
        5,
        5,
        150,
        2
    )


    temp_width = display.measure_text(
        temperature,
        3
    )

    display.text(
        temperature,
        296 - temp_width - 5,
        5,
        90,
        3
    )


    display.line(
        0,
        28,
        296,
        28
    )


    # BIN

    display.text(
        bin_name,
        5,
        40,
        120,
        3
    )


    display.text(
        date,
        5,
        80,
        120,
        2
    )


    display.text(
        days,
        5,
        105,
        150,
        2
    )


    # WEATHER

    rain_text = "RAIN " + rain


    rain_width = display.measure_text(
        rain_text,
        2
    )


    display.text(
        rain_text,
        296 - rain_width - 5,
        55,
        130,
        2
    )


    draw_weather_icon(
        condition,
        255,
        100
    )


    display.update()