from rest_framework import serializers
from . import models


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
