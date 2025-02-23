import requests

import json

from datetime import datetime


def time_from_utc_with_timezone(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


#Enter your city name

city_name = input("Enter the city name : ")


#Enter your api key

api_key = "26c2425b238c58c09462c029b85e0cd4"


#Api url

weather_url = "http://api.openweathermap.org/data/2.5/weather?" + "&q="+city_name + "&appid=" +api_key


response = requests.get(weather_url)

weather_data = response.json()

print(weather_data)

if weather_data['cod'] == 200:
    kelvin = 273.15
    temp = int(weather_data['main']['temp'] - kelvin)
    feels_like = int(weather_data['main']['feels_like'] - kelvin)
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed'] * 3.6
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']
    timezone = weather_data['timezone']
    cloudy = weather_data['clouds']['all']
    description = weather_data['weather'][0]['description']
    
    
    
    sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
    sunset_time = time_from_utc_with_timezone(sunset + timezone)
    
    print("\n-----------Weather Information Using API---------")
    print(f"Weather information for : {city_name}")
    print(f"Temperature (C) : {temp}")
    print(f"Feels like in (celsius):{feels_like}")
    print(f"Pressure:{pressure}hpa")
    print(f"Humidity:{humidity}hpa")
    print(f"Wind_Speed:{wind_speed}")
    print(f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
    print(f"Cloudy: {cloudy}%")
    print(f"Info: {description}")

else:
    print(f"City_name: {city_name} was not found")