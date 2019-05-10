import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectaudit.settings')

app = Celery('projectaudit')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()