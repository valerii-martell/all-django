"""
ASGI config for LESSON_10 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

import channels_app.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "all_django.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(channels_app.routing.websocket_urlpatterns))
        ),
    }
)
