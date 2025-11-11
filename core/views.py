# core/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from projects.models import Project
from blog.models import Post


def home(request):
    return render(request, "home.html")


def home(request):
    # show featured projects, latest posts
    featured = Project.objects.filter(featured=True)[:3]
    latest_projects = Project.objects.all()[:6]
    latest_posts = Post.objects.all()[:3]
    context = {"featured": featured, "projects": latest_projects, "posts": latest_posts}
    return render(request, "home.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks — your message has been received. I will get back to you soon.",
            )
            return redirect("contact")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
