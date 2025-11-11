from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "published_at")  # ✅ now valid
    prepopulated_fields = {"slug": ("title",)}
