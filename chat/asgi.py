"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')
django_asgi_app = get_asgi_application()

# 프로토콜 타입별로 서로 다른 ASGI application을 처리하도록 라우팅 설정 변경
# application = get_asgi_application()
application = ProtocolTypeRouter({
    # 지금은 http 타입에 대한 라우팅만 명시
    "http": django_asgi_app
    # 서비스 규모에 따라 http와 websocket을 분리하여 (웹서버와 채팅서버) 운영 가능
    # "websocket": ...
})
