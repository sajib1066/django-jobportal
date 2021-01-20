from django.shortcuts import render


def job_post(request):
    return render(request, 'job-section/job-post.html')


def job_find(request):
    return render(request, 'job-section/find-job.html')
