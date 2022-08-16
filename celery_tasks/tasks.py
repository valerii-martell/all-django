import requests
from celery import shared_task

from all_django.celery import app


@app.task
def fibon(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@shared_task
def fetch_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5b9dee532cf418833e63baf01e31e197'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(
        city)).json()
    return city_weather.get('wind')
