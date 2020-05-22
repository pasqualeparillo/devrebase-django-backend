from django.http import JsonResponse
import django_filters.rest_framework
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from .serializers import JobSerializer, CompanySerializer, TokenSerializer
from .models import Job
from django.db.models import Count, Sum
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Pagination for job listings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


@api_view()
def null_view(request):
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
class GoogleLogin(SocialLoginView):
    authentication_classes = (JSONWebTokenAuthentication,)
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
          
class ListJobPagination(PageNumberPagination):
    page_size = 20  # Number of objects to return in one page

# List view for job postings with job pagination limit of 20


class ListJob(generics.ListAPIView):
    pagination_class = ListJobPagination
    serializer_class = JobSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self, **kwargs):
        jobs = Job.objects.all()
        return jobs

# detail view for job postings


class DetailJob(generics.RetrieveAPIView):
    pagination_class = ListJobPagination
    serializer_class = JobSerializer
    lookup_fields = ('id')

    def get_queryset(self, **kwargs):
        jobs = Job.objects.all()
        return jobs

# Search view for job postings


class SearchList(generics.ListAPIView):
    pagination_class = ListJobPagination
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('job_title', 'job_body')

# view for listing popular companies


class ListCompany(generics.ListAPIView):
    pagination_class = ListJobPagination
    serializer_class = JobSerializer

    def get_queryset(self):
        company = self.kwargs['job_company']
        return Job.objects.all().filter(company_name=company)


class CompanyCount(generics.ListAPIView):
    pagination_class = ListJobPagination
    serializer_class = CompanySerializer
    queryset = Job.objects.all()

    def get_queryset(self):
        return Job.objects.values('job_company').annotate(
            companies=Count('job_company'),
        ).order_by('-companies')[:20]


# View for adding/removing as favorite
@api_view(['GET'])
def FavoriteJob(request, id):
    job = get_object_or_404(Job, id=id)
    # Check if user is in favorite list on model & remove if so.
    if job.favorite.filter(id=request.user.id).exists():
        job.favorite.remove(request.user)
        return Response({"Favorite": "Removed"}, status=status.HTTP_200_OK)
    # else add if not in favorite list
    else:
        user = request.user
        job.favorite.add(user)
        return Response({"Favorite": "Added"}, status=status.HTTP_200_OK)

# Request current user, get favorite posts for user & filter JobSerializer for posts.
@api_view(['GET'])
def FavoriteList(request):
    user = request.user
    favorite_posts = user.favorite.all()
    serializer = JobSerializer(favorite_posts, many=True)
    return Response({"Favorites": serializer.data}, status=status.HTTP_200_OK)
