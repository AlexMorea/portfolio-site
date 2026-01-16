from django.urls import path
from . import views
from core.views import fix_admin

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("fix-admin-temp/", fix_admin, name="fix_admin_temp"),
]
