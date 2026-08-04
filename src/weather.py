import requests


LATITUDE = 53.481
LONGITUDE = -2.121


def get_weather():

    try:

        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=" + str(LATITUDE)
            + "&longitude=" + str(LONGITUDE)
            + "&current=temperature_2m,weather_code"
            + "&hourly=precipitation_probability"
        )

        response = requests.get(url)

        data = response.json()

        response.close()


        temperature = data["current"]["temperature_2m"]

        weather_code = int(
            data["current"]["weather_code"]
        )

        rain_chance = data["hourly"]["precipitation_probability"][0]


        return {
            "temperature": str(round(temperature)) + "C",
            "condition": weather_description(weather_code),
            "rain": str(rain_chance) + "%"
        }


    except Exception as e:

        print("Weather error:")
        print(e)

        return {
            "temperature": "--C",
            "condition": "Offline",
            "rain": "--"
        }



def weather_description(code):

    descriptions = {

        0: "Sunny",

        1: "Mainly Clear",
        2: "Part Cloudy",
        3: "Cloudy",

        45: "Fog",
        48: "Fog",

        51: "Drizzle",
        53: "Drizzle",
        55: "Drizzle",

        61: "Rain",
        63: "Rain",
        65: "Heavy Rain",

        71: "Snow",
        73: "Snow",
        75: "Heavy Snow",

        80: "Showers",
        81: "Showers",
        82: "Heavy Showers",

        95: "Storm",
        96: "Storm",
        99: "Storm"
    }


    return descriptions.get(code, "Unknown")