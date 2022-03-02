from django.shortcuts import render, get_object_or_404
from .models import Projects

def home(request):
    projects = Projects.objects.all()
    return render(request, "projects/index.html", {"projects": projects})