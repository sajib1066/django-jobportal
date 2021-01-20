from django.shortcuts import render


def contact_page(request):
    return render(request, 'contact/contact.html')
