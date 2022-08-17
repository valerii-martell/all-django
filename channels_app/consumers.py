import json
from datetime import datetime

from channels.db import database_sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer

from channels_app.models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        print(self.channel_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        self.user = self.scope["user"]
        await self.accept()
        data = await self.get_historical_data()

        for message_obj in data:
            await self.send(text_data=json.dumps({
                'message': message_obj.text,
                'date': str(message_obj.timestamp),
                'user': message_obj.user.username,
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.new_message(message=message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message,
            'date': str(datetime.now()),
            'user': self.user.username
        }))

    @database_sync_to_async
    def new_message(self, message):
        Message.objects.create(text=message, user=self.user,
                               room=Room.objects.get(name=self.room_name))

    @database_sync_to_async
    def get_historical_data(self):
        return Message.objects.filter(room=Room.objects.get(name=self.room_name))


class LikesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        like = text_data_json.get('like', None)
        dislike = text_data_json.get('dislike', None)
        if like:
            await self.new_like()
        if dislike:
            await self.new_dislike()

    @database_sync_to_async
    def new_like(self):
        room_instance = Room.objects.get(name=self.room_name)
        room_instance.likes += 1
        room_instance.save()

    @database_sync_to_async
    def new_dislike(self):
        room_instance = Room.objects.get(name=self.room_name)
        room_instance.dislikes += 1
        room_instance.save()
