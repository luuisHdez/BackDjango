import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import os


# Create your views here.
@require_GET
def OpenWeather(request):
    api_key_path = os.path.join(os.path.dirname(__file__), 'openweather_api_key.txt')

    #Read the API key from the file
    with open(api_key_path, 'r') as file: 
      api_key = file.read().strip()
      print(api_key, "api_key")

    #api_key = '967e5b6efc2d04f83a9a1c88a1fa4d7e'

    city = request.GET.get('city', 'Xalapa')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'Infector': 'Me la super Pelaaaan jaja'
        }
        print(weather_data, 'weather_data')
    else: 
        weather_data = {'error': 'City not found or some error ocurred'}

    return JsonResponse(weather_data)
    PpqtRaaduRf8Evpd