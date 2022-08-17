import json
from datetime import date

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

        for timestamp, message in data.items():
            await self.send(text_data=json.dumps({
                'message': message,
                'date': str(timestamp),
                'user': self.user.username,
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
            'date': str(date.today()),
            'user': self.user.username
        }))

    @database_sync_to_async
    def new_message(self, message):
        Message.objects.create(text=message, user=self.user,
                               room=Room.objects.get(name=self.room_name))

    @database_sync_to_async
    def get_historical_data(self):
        return dict(
            Message.objects.filter(user=self.user,
                                   room=Room.objects.get(
                                       name=self.room_name)).values_list(
                'timestamp',
                'text'))
