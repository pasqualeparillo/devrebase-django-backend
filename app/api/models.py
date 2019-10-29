from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return(self.user.username)


class Job(models.Model):
    job_company = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    job_body = models.TextField(blank=True)
    job_url = models.TextField(blank=True)
    job_source = models.CharField(max_length=30, blank=True)
    job_location = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True)
    favorite = models.ManyToManyField(
        User, related_name='favorite', blank=True)

    def __str__(self):
        return(self.job_title)
