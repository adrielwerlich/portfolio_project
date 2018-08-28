from django.shortcuts import render
from .models import Job
# Create your views here.

def showJobsHome(request):
    jobsValues = Job.objects
    return render(request, 'jobs_home_page.html', {'jobsKeys': jobsValues})