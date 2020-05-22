from django.core.management.base import BaseCommand, CommandError
from api.models import Job
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete objects older than 30 days'
    def handle(self, *args, **options):
        Jobs = Job.objects.all()
        for i in Jobs:
            if i.expiration_date < timezone.now() + timedelta(days=30):
                i.delete()
        return self.stdout.write('Deleted objects older than 30 days')