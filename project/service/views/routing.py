from django.urls import path, include
from .consumer import ChatConsumer

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    path("chat", ChatConsumer.as_asgi()),
]
'''
path("chat", ChatConsumer.as_asgi()): 
"chat" 경로로 들어오는 WebSocket 요청을 ChatConsumer 클래스의 ASGI 애플리케이션으로 라우팅합니다.
'''
