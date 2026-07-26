def format_date(date):

    if not date:
        return "Unknown"

    year, month, day = date

    return f"{day}/{month}"