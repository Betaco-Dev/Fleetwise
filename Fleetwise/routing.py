from django.urls import re_path
from . import consumers  # consumers.py will contain your websocket logic

websocket_urlpatterns = [
    re_path(r'ws/somepath/$', consumers.YourConsumer.as_asgi()),
]
