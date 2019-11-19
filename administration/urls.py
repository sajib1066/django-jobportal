from django.urls import path
from .views import login_page, register_page

urlpatterns = [
    path('candidate/login', login_page, name='candidate-login'),
    path('candidate/register', register_page, name='candidate-register')
]
