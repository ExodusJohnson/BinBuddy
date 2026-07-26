import time


# Tameside collection schedule
# Format:
# (year, month, day, bins)

COLLECTIONS = [
    (2026, 7, 30, ["Green"]),

    (2026, 8, 6, ["Black"]),
    (2026, 8, 13, ["Green", "Blue"]),
    (2026, 8, 20, []),
    (2026, 8, 27, ["Black", "Green"]),

    (2026, 9, 3, ["Blue"]),
    (2026, 9, 10, ["Green"]),
    (2026, 9, 17, ["Black"]),
    (2026, 9, 24, ["Green", "Blue"]),
]


def get_next_collection():

    now = time.localtime()

    today = (
        now[0],
        now[1],
        now[2]
    )

    for year, month, day, bins in COLLECTIONS:

        collection_date = (
            year,
            month,
            day
        )

        if collection_date >= today:

            return {
                "date": collection_date,
                "bins": bins
            }


    return {
        "date": None,
        "bins": []
    }


def format_bins(bins):

    if not bins:
        return "No bins"

    names = []

    for bin_type in bins:

        if bin_type == "Black":
            names.append("BLACK")

        elif bin_type == "Green":
            names.append("GREEN")

        elif bin_type == "Blue":
            names.append("BLUE")

        else:
            names.append(bin_type.upper())

    return " + ".join(names)