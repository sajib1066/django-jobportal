from django.urls import path
from .views import blog_page

urlpatterns = [
    path('', blog_page, name='blog')
]
