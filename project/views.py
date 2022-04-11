from django.shortcuts import render
from main.models import projects

# Create your views here.


def homepage(request):
    return render(request, template_name='main/home.html')


def projectspage(request):
    project = projects.objects.all()
    return render(request, template_name='main/projects.html', context={'projects': project})
