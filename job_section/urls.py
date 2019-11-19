from django.urls import path
from .views import job_post

urlpatterns = [
    path('post', job_post, name='job-post')
]
