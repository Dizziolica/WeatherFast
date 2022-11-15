import requests

API_KEY = "da4cd2c152e015add1aee77ca9725268"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the big city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
data = response.json()
if response.status_code == 200:

    weather = data['weather'][0]['description']
    print(weather)
    temperature =round(data['main']['temp']-273.15, 2)
    print("Weather", weather)
    print("Temperature", temperature, "Celsius")
else:
    print("An error occurred")