from django.shortcuts import render

# Create your views here.
def candidates_page(request):
    return render(request, 'candidates/candidates.html')
