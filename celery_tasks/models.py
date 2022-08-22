from django.db import models


class Bot(models.Model):
    password = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=32, blank=True, null=True)
