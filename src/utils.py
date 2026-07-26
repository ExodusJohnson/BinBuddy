MONTHS = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def format_date(date):

    if not date:
        return "Unknown"

    year, month, day = date

    return f"{day} {MONTHS[month]}"