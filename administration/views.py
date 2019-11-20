from django.shortcuts import render

# Create your views here.
def candidate_login_page(request):
    return render(request, 'administration/candidate-login.html')

def candidate_register_page(request):
    return render(request, 'administration/candidate-register.html')

def employee_login_page(request):
    return render(request, 'administration/employee-login.html')

def employee_register_page(request):
    return render(request, 'administration/employee-register.html')
