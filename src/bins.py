import time


# Tameside collection schedule
# Brown bins ignored
# Format:
# (year, month, day, bins)


COLLECTIONS = [

    # 2026

    (2026, 1, 15, ["Green", "Blue"]),
    (2026, 1, 22, []),
    (2026, 1, 29, ["Black", "Green"]),

    (2026, 2, 5, ["Blue"]),
    (2026, 2, 12, ["Green"]),
    (2026, 2, 19, ["Black"]),
    (2026, 2, 26, ["Green", "Blue"]),

    (2026, 3, 5, []),
    (2026, 3, 12, ["Black", "Green"]),
    (2026, 3, 19, ["Blue"]),
    (2026, 3, 26, ["Green"]),

    (2026, 4, 2, ["Black"]),
    (2026, 4, 9, ["Green", "Blue"]),
    (2026, 4, 16, []),
    (2026, 4, 23, ["Black", "Green"]),
    (2026, 4, 30, ["Blue"]),

    (2026, 5, 7, ["Green"]),
    (2026, 5, 14, ["Black"]),
    (2026, 5, 21, ["Green", "Blue"]),
    (2026, 5, 28, []),

    (2026, 6, 4, ["Black", "Green"]),
    (2026, 6, 11, ["Blue"]),
    (2026, 6, 18, ["Green"]),
    (2026, 6, 25, ["Black"]),

    (2026, 7, 2, ["Green", "Blue"]),
    (2026, 7, 9, []),
    (2026, 7, 16, ["Black", "Green"]),
    (2026, 7, 23, ["Blue"]),
    (2026, 7, 30, ["Green"]),

    (2026, 8, 6, ["Black"]),
    (2026, 8, 13, ["Green", "Blue"]),
    (2026, 8, 20, []),
    (2026, 8, 27, ["Black", "Green"]),

    (2026, 9, 3, ["Blue"]),
    (2026, 9, 10, ["Green"]),
    (2026, 9, 17, ["Black"]),
    (2026, 9, 24, ["Green", "Blue"]),

    (2026, 10, 1, []),
    (2026, 10, 8, ["Black", "Green"]),
    (2026, 10, 15, ["Blue"]),
    (2026, 10, 22, ["Green"]),
    (2026, 10, 29, ["Black"]),

    (2026, 11, 5, ["Green", "Blue"]),
    (2026, 11, 12, []),
    (2026, 11, 19, ["Black", "Green"]),
    (2026, 11, 26, ["Blue"]),

    (2026, 12, 3, ["Green"]),
    (2026, 12, 10, ["Black"]),
    (2026, 12, 17, ["Green", "Blue"]),
    (2026, 12, 24, []),


    # 2027

    (2027, 1, 14, ["Green"]),
    (2027, 1, 21, ["Black"]),
    (2027, 1, 28, ["Green", "Blue"]),

    (2027, 2, 4, []),
    (2027, 2, 11, ["Black", "Green"]),
    (2027, 2, 18, ["Blue"]),
    (2027, 2, 25, ["Green"]),

    (2027, 3, 4, ["Black"]),
    (2027, 3, 11, ["Green", "Blue"]),
    (2027, 3, 18, []),
    (2027, 3, 25, ["Black", "Green"]),

    (2027, 4, 1, ["Blue"]),
    (2027, 4, 8, ["Green"]),
    (2027, 4, 15, ["Black"]),
    (2027, 4, 22, ["Green", "Blue"]),
    (2027, 4, 29, []),

    (2027, 5, 6, ["Black", "Green"]),
    (2027, 5, 13, ["Blue"]),
    (2027, 5, 20, ["Green"]),
    (2027, 5, 27, ["Black"]),

    (2027, 6, 3, ["Green", "Blue"]),
    (2027, 6, 10, []),
    (2027, 6, 17, ["Black", "Green"]),
    (2027, 6, 24, ["Blue"]),

    (2027, 7, 1, ["Green"]),
    (2027, 7, 8, ["Black"]),
    (2027, 7, 15, ["Green", "Blue"]),
    (2027, 7, 22, []),
    (2027, 7, 29, ["Black", "Green"]),
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


    if not names:
        return "No bins"


    return " + ".join(names)