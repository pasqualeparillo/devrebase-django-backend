from celery import shared_task
from api.models import Job
from datetime import datetime, timedelta
from django.utils import timezone

def some_task():
    Jobs = Job.objects.all()
    for i in Jobs:
        if i.expiration_date < timezone.now() + timedelta(days=31):
            i.delete()
    return "completed deleting foos at {}".format(timezone.now())