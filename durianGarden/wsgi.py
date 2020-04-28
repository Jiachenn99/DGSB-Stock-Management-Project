"""
WSGI config for durianGarden project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
os.environ['DB_PASSWORD'] = "initialize#"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'durianGarden.settings')

application = get_wsgi_application()
