#Contains websockets logic
from channels.generic.websocket import AsyncWebsocketConsumer 
import json

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({'message': 'WebSocket connected!'}))

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle incoming messages here
        await self.send(text_data=json.dumps({'response': 'Message received'}))
