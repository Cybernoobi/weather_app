import requests
from pprint import pprint
from .utils import convert_seconds_to_date
from db import querise as sql
import json
import config


def get_weather():
    data = []

    username = input('ТЫ КТО?: ')
    if not sql.check_user_exists('weather.db', username):
        sql.add_user('weather.db', username)
        get_weather()
    else:
        while True:
            city = input("Напишите свой город: ")

            if city == "save":
                with open("weather.json", mode="w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
                continue

            config.parameters["q"] = city

            resp = requests.get(config.url, params=config.parameters).json()
            pprint(resp)  # dt, sunrise, sunset, timezone, name, description, speed
            tz = resp["timezone"]
            name = resp["name"]
            sunrise = convert_seconds_to_date(seconds=resp["sys"]["sunrise"], timezone=tz)
            sunset = convert_seconds_to_date(seconds=resp["sys"]["sunset"], timezone=tz)
            dt = convert_seconds_to_date(seconds=resp["dt"], timezone=tz)
            print(resp["timezone"])
            description = resp["weather"][0]["description"]
            speed = resp["wind"]["speed"]
            temp = resp["main"]["temp"]
            data.append(
                dict(
                    zip(
                        ["name", "sunrise", "sunset", "description", "speed"],
                        [name, sunrise, sunset, description, speed]
                    )
                )
            )

            print(f"""
=====================================
В городе {name} сейчас {description}
Температура: {temp}
Скорость ветра: {speed}
Восход солнца: {sunrise}
Закат солнца: {sunset}
Время отправки запроса: {dt}
=====================================
""")
