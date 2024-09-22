# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configuración de Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

# Cargar configuración desde settings.py usando la clave CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover de tareas
app.autodiscover_tasks()