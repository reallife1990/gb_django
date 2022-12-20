import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
celery_app = Celery("brainiac")
celery_app.config_from_object("django.conf:setting", namespace="CELERY")
celery_app.autodiscover_tasks()
