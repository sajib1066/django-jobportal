from django.shortcuts import render


def candidates_page(request):
    return render(request, 'candidates/candidates.html')
