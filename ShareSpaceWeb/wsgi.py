"""
WSGI config for ShareSpaceWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ShareSpaceWeb.settings")
os.environ["SECRET_KEY"] = '36&l_!ilukc6l@3g)20v)4jzv$0_x0a(%up0%(4=6fa^zmos_l'

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
