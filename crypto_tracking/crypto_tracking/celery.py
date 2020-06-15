import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_tracking.settings')

app = Celery('crypto_tracking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()