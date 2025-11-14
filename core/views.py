from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ContactForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "project_detail.html", {"project": project})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
