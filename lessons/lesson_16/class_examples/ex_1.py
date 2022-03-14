import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q": "Chisinau,MD", "lang": "null", "units": "metric", "mode": "json"}
# q for the location to search
# lang: language for the response (Default English)
# units: metric or imperial (Celsius or Fahrenheit)
# mode: json/xml/text - how to return the information

headers = {
    'x-rapidapi-key': "REMOVED"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
print(data['coord'])
# {'lon': 28.8575, 'lat': 47.0056}
print(data['weather'])
# [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]
print(data['main'])
# {'temp': 2.42, 'feels_like': -1.03, 'temp_min': 1.63, 'temp_max': 2.74, 'pressure': 1032, 'humidity': 68}
