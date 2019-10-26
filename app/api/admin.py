from django.contrib import admin
from api.models import Profile, Posting

admin.site.register(Profile)
admin.site.register(Posting)
class PostingAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'