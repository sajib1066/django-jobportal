from django.shortcuts import render


def about_page(request):
    return render(request, 'about/about.html')
