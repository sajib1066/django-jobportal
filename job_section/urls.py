from django.urls import path
from .views import job_post, job_find

urlpatterns = [
    path('post', job_post, name='job-post'),
    path('find', job_find, name='job-find')
]
