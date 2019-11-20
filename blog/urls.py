from django.urls import path
from .views import blog_page, blog_details

urlpatterns = [
    path('', blog_page, name='blog'),
    path('details', blog_details, name='blog-details')
]
