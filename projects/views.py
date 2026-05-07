from django.shortcuts import render
from django.http import HttpResponse
from .data import PROJECTS



def project_list(request):
    return render(request, "projects.html", {
        "projects": PROJECTS
    })


def project_detail(request, slug):
    project = next(
        (p for p in PROJECTS if p["slug"] == slug),
        None
    )

    if not project:
        return HttpResponse("Project not found")

    return render(request, "project_detail.html", {
        "project": project
    })