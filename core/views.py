from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def projects(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
