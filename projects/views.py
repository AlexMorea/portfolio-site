# projects/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects_list.html", {"projects": projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "project_detail.html", {"project": project})
