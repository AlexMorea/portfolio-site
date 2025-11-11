# projects/models.py
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError


def validate_slug_unique(value):
    if not value:
        raise ValidationError("Slug cannot be empty.")


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField(blank=True)
    repo_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # auto-generate slug if missing
        if not self.slug:
            base = slugify(self.title)[:50]
            self.slug = base
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("project_detail", args=[self.slug])
