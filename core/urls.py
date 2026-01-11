from django.urls import path
from . import views
from core.views import create_temp_admin

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("create-admin-temp/", create_temp_admin),
]
