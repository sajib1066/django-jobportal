from django.urls import path
from .views import candidates_page

urlpatterns = [
    path('', candidates_page, name='candidates')
]
