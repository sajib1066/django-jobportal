from django.urls import path
from .views import candidate_login_page, candidate_register_page, employee_login_page, employee_register_page

urlpatterns = [
    path('candidate/login', candidate_login_page, name='candidate-login'),
    path('candidate/register', candidate_register_page, name='candidate-register'),
    path('employee/login', employee_login_page, name='employee-login'),
    path('employee/register', employee_register_page, name='employee-register')
]
