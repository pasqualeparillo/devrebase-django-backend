from rest_framework import serializers
from . import models
from allauth.socialaccount.models import SocialToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = (
            'user'
        )
        
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialToken
        fields = (
         'account',
         'token',
        )

class JobSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)
    class Meta:
        ordering = ['-id']
        model = models.Job
        fields = (
            'id',
            'job_company',
            'job_title',
            'job_body',
            'job_url',
            'job_source',
            'job_location',
            'favorite',
            'created_date',
            'expiration_date'
        )

class CompanySerializer(serializers.ModelSerializer):
    companies = serializers.IntegerField()
    class Meta:
        model = models.Job
        fields = (
            'id',
            'companies',
            'job_company',
        )
