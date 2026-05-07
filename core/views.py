from django.shortcuts import render, redirect
from .forms import ContactForm

# IMPORT STATIC PROJECT DATA
from projects.data import PROJECTS


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


# PROJECT LIST
def projects(request):
    return render(request, "projects.html", {
        "projects": PROJECTS
    })


# PROJECT DETAIL
def project_detail(request, project_id):
    project = next(
        (p for p in PROJECTS if p["id"] == project_id),
        None
    )

    return render(request, "project_detail.html", {
        "project": project
    })


# CONTACT PAGE
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form
    })