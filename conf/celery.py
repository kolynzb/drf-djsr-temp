import os

from celery import Celery

from conf.settings import base

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.development')

celery = Celery('config')
celery.config_from_object('django.conf:settings.development', namespace='CELERY')
celery.autodiscover_tasks(lambda: base.INSTALLED_APPS)