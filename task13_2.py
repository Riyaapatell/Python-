# weather api
import requests

api_key = "8613f15eda2c9291eb0ba3e4d47a823d"

city = input("Enter city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Minimum Temperature:", data["main"]["temp_min"], "°C")
    print("Maximum Temperature:", data["main"]["temp_max"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Cloudiness:", data["clouds"]["all"], "%")
    print("Visibility:", data["visibility"], "m")
else:
    print("Entered city DNE./Entered a valid city.")