# Portfolio/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import fix_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("fix-admin-temp/", fix_admin),
    path("", include("core.urls")),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
]
