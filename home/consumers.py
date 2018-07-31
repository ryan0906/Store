from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache import cache
import json


class Consumer(AsyncWebsocketConsumer):
    room_group_name = ''

    async def connect(self):
        self.room_group_name = 'connections'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if 'conv' in cache:
            old_conv = cache.get('conv')
        else:
            old_conv = ""
        cache.set('conv', old_conv + message, 300)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'order_list',
                'message': message
            }
        )

    async def order_list(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))