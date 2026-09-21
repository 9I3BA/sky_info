import requests

API_KEY = "9900135cedc55a0db486b8bf9fe01b02"
CITY_NAME = "Цивильск"
LANGUAGE = "ru"
UNITS = "metric"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&lang={LANGUAGE}&units={UNITS}"
try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        print(f"Погода в городе {CITY_NAME}:")
        print(f"На улице: {description}")
        print(f"Температура: {temp}°C (ощущается как {feels_like}°C)")
    else:
        print(f"Не удалось получить данные. Код ошибки: {response.status_code}")
        print(f"Причина: {data.get('message')}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка сети: {e}")
