from django.urls import path
from .views import OpenWeather

urlpatterns = [
    path('open-weather/', OpenWeather, name='open-weather')
]
