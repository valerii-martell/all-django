from django.urls import path
from . import views

urlpatterns = [
    path('', views.channels_index, name='channels_index'),
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
]