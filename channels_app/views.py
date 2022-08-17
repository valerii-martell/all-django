from django.shortcuts import render
from .models import Room


def channels_index(request):
    lobby, _ = Room.objects.get_or_create(name="lobby", likes=0, dislikes=0)
    return render(request, 'channels_index.html', {})


def chat(request):
    rooms = Room.objects.all()
    return render(request, 'chat/chat.html', {'rooms':rooms})


def room(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    # messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room_name': room_name,
        # 'messages': messages,
    })

