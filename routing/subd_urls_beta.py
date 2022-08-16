from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.beta, name='beta'),
]