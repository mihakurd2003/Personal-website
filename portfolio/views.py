from django.shortcuts import render
from .models import Project


def home(request):
    portfolio_project = Project.objects.all()
    return render(request, 'portfolio/home.html', {'portfolio_project': portfolio_project})
