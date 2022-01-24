"""
WSGI config for mmysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from . import settings
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/mmysite')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/myproject/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mmysite.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()