import requests
import os
API_KEY = "9900135cedc55a0db486b8bf9fe01b02"
LANGUAGE = "ru"
UNITS = "metric"
FILENAME = "citys.txt"

while True:
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        city_name = input("Файл пуст. Введите название города: ").strip()
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.write(city_name)
    else:
        with open(FILENAME, "r", encoding="utf-8") as file:
            city_name = file.read().strip()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang={LANGUAGE}&units={UNITS}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]
            print(f"Погода в городе {city_name}:")
            print(f"На улице: {description}")
            print(f"Температура: {temp}°C (ощущается как {feels_like}°C)")
            edit_city = input("Чтобы изменить город напишите \"да\"(или нажмите Enter, чтобы выйти): ").strip().lower()
            if edit_city == "да":
                new_city = input("Введите название нового города: ").strip()
                with open(FILENAME, "w", encoding="utf-8") as file:
                    file.write(new_city)
                print("Город изменен. Обновляем данные...\n")
                continue
            else:
                print("Программа завершена")
                break

        else:
            print(f"Не удалось получить данные. Код ошибки: {response.status_code}")
            print(f"Причина: {data.get('message')}")
            if response.status_code == 404 and os.path.exists(FILENAME):
                os.remove(FILENAME)
            break

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
        break