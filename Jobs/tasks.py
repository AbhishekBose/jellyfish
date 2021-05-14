from celery import shared_task
import time

@shared_task
def celery_task(duration):
    time.sleep(duration)
    return None
    