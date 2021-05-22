from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import json

from .models import *


class ChatConsumerAsync(AsyncWebsocketConsumer):

    async def connect(self):

        print("def connect(self):")

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_'+str(self.room_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()


    async def disconnect(self, message):

        print("def disconnect(self, message):")

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)


    async def receive(self, *, text_data):

        print("def recieve(self, *, text_data):")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await sync_to_async(ChatModel(room_no=self.room_name, message=message).save)()

        await self.channel_layer.group_send(self.room_group_name, {'message': message,'type': 'send_back' })

    async def send_back(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))


class ChatConsumerSync(WebsocketConsumer):

    def connect(self):

        print("def connect(self):")

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_'+str(self.room_name)
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()


    def disconnect(self, message):

        print("def disconnect(self, message):")

        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)


    def receive(self, *, text_data):

        print("def recieve(self, *, text_data):")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(ChatModel(room_no=self.room_name, message=message).save)()

        async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'message': message,'type': 'send_back' })

    def send_back(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'message': message}))