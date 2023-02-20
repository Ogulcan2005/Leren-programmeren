import requests

APP_ID = 'a352db877902bafba7d0ed23e766033'
url = 'https://api.openweathermap.org/data/2.5/weather?q=Dordrecht&appid=' + APP_ID
response = requests.get(url)

json_response = response.json()
print(type(json_response))
print(json_response)
