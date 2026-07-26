import time


def format_date(date):

    if not date:
        return "Unknown"

    year, month, day = date

    return f"{day}/{month}"


def days_until(date):

    if not date:
        return ""

    now = time.localtime()

    today = time.mktime(
        (
            now[0],
            now[1],
            now[2],
            0,
            0,
            0,
            0,
            0
        )
    )

    target = time.mktime(
        (
            date[0],
            date[1],
            date[2],
            0,
            0,
            0,
            0,
            0
        )
    )

    days = int((target - today) / 86400)

    if days == 0:
        return "TODAY"

    elif days == 1:
        return "TOMORROW"

    else:
        return f"IN {days} DAYS"