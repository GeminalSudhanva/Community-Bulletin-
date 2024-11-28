import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from api.consumers import PostConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'community_bulletin_board.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # Example WebSocket URL routing
            path("ws/posts/", PostConsumer.as_asgi()),
        ])
    ),
})
