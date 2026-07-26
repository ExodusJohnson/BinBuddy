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
        weather_code = data["current"]["weather_code"]

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

    if code == 0:
        return "Sunny"

    elif code in [1, 2, 3]:
        return "Cloudy"

    elif code in [45, 48]:
        return "Fog"

    elif code in [51, 53, 55]:
        return "Drizzle"

    elif code in [61, 63, 65]:
        return "Rain"

    elif code in [71, 73, 75]:
        return "Snow"

    elif code >= 95:
        return "Storm"

    else:
        return "Unknown"