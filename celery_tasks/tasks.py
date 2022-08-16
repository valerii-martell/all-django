import requests
import string

from django.utils.crypto import get_random_string
from celery import shared_task
from all_django.celery import app
from .models import Bot


@app.task
def fibonacci(n):
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


@shared_task
def create_bot(total):
    for _ in range(total):
        email = f'{get_random_string(31, string.ascii_letters)}@gmail.com'
        password = get_random_string(50)
        Bot.objects.create(email=email, password=password)
    return f'{total} random bots created'
