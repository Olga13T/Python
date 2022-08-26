import datetime
import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    code_emodji = {
        "Clear":"Ясно \U0002600",
        "Clouds":"Облачно \U0002601",
        "Rain": "Дождь \U+0002614",
        "Snow": "Снег \U0002744"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        # pprint(data) #распечатает всю информацию
        
        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_emodji:
            wd = code_emodji[weather_description]
        else:
            wd = "Требуется уточнение..."
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        print(f"{datetime.datetime.now().strftime('%Y-%n-%d %H:%M')}\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C {wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure}мм.рт.ст\nСкорость ветра: {wind}м/с")

    except Exception as ex:
        print(ex)
        print("Check the city please")


def main():
    city = input("Enter the city: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
