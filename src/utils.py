import time


def format_date(date):

    year, month, day = date

    weekdays = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

    weekday_number = time.localtime(
        time.mktime(
            (year, month, day, 0, 0, 0, 0, 0, 0)
        )
    )[6]

    weekday = weekdays[weekday_number]

    return "{} {:02d}/{:02d}".format(
        weekday,
        day,
        month
    )


def days_until(date):

    now = time.localtime()

    today = (
        now[0],
        now[1],
        now[2]
    )

    target = (
        date[0],
        date[1],
        date[2]
    )

    today_seconds = time.mktime(
        (
            today[0],
            today[1],
            today[2],
            0,
            0,
            0,
            0,
            0,
            0
        )
    )

    target_seconds = time.mktime(
        (
            target[0],
            target[1],
            target[2],
            0,
            0,
            0,
            0,
            0,
            0
        )
    )

    days = int(
        (target_seconds - today_seconds) / 86400
    )


    if days == 0:
        return "TODAY"

    elif days == 1:
        return "IN 1 DAY"

    else:
        return "IN {} DAYS".format(days)