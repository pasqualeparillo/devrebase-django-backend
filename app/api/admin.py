from django.contrib import admin
from api.models import Profile, Job

admin.site.register(Profile)
admin.site.register(Job)
class JobAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'