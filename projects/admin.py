# projects/admin.py
from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "featured", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "short_description")
