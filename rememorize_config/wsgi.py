"""
WSGI config for rememorize_config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv, find_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rememorize_config.settings')
load_dotenv(find_dotenv())

application = get_wsgi_application()
