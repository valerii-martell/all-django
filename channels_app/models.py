from django.db import models
from django.contrib.auth import get_user_model


class Room(models.Model):
    name = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', null=True,
                             on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), null=True, blank=True,
                             on_delete=models.CASCADE)