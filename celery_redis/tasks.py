import requests
from celery import shared_task

from all_django.celery import app


@app.task
def fibon(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
