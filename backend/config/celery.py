import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

# Create a Celery application instance named 'renting'.
app = Celery('renting')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    # A debug task that prints the request information.
    print(f'Request: {self.request!r}')

# This file configures Celery to work with Django framework.
# It sets up the default Django settings module, creates a Celery app
# named 'renting', configures it from Django settings, and
# auto-discovers tasks from installed Django apps.
# The debug_task function is a simple example Celery task which prints
# information about the task request when executed.
