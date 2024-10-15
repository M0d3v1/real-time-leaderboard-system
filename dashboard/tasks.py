# dashboard/tasks.py

from celery import shared_task
import time

@shared_task
def sample_task(duration):
    time.sleep(duration)
    return f'Slept for {duration} seconds'
