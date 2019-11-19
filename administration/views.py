from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'administration/login.html')

def register_page(request):
    return render(request, 'administration/register.html')
