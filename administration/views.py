from django.shortcuts import render

# Create your views here.
def candidate_login_page(request):
    return render(request, 'administration/login.html')

def candidate_register_page(request):
    return render(request, 'administration/register.html')
