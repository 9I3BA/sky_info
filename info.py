import requests
import os

API_KEY = "9900135cedc55a0db486b8bf9fe01b02"
LANGUAGE = "ru"
UNITS = "metric"
FILENAME = "citys.txt"

def load_city():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return None
    with open(FILENAME, "r", encoding="utf-8") as file:
        return file.read().strip()

def save_city(city_name: str):
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write(city_name.strip())

def get_weather(city_name: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang={LANGUAGE}&units={UNITS}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            return {
                "ok": True,
                "city": city_name,
                "temp": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "description": data["weather"][0]["description"]
            }
        else:
            return {
                "ok": False,
                "error": data.get("message", "Неизвестная ошибка"),
                "code": response.status_code
            }

    except requests.exceptions.RequestException as e:
        return {
            "ok": False,
            "error": f"Ошибка сети: {e}",
            "code": None
        }
