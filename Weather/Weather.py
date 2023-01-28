from webbrowser import get
import requests

API_KEY = "8c37a02f1ae12a05127d8c6ef3c2ddce"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occured.")