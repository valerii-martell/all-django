from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<room_name>/", consumers.ChatConsumer.as_asgi()),
    path("ws/likes/<room_name>/", consumers.LikesConsumer.as_asgi()),
]
