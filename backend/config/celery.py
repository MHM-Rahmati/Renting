import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

# Create a Celery application instance named 'renting'.
app = Celery('renting')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings.dev', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Define a debug task that prints the request information.
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    # A debug task that prints the request information.
    print(f'Request: {self.request!r}')

# This file configures Celery to work with the Django framework.
# It sets up the default Django settings module, creates a Celery app with
# the name 'renting', configures it from the Django settings using the
# 'CELERY' namespace, and enables task autodiscovery from installed apps.
# It also defines a simple debug task for logging request details during task execution.
