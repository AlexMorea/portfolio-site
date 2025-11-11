from django.shortcuts import render, get_object_or_404
from .models import Post  # We'll create this model soon


def post_list(request):
    return render(request, "blog/post_list.html")


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
