from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="projects_list"),
    path("api/", views.ProjectListAPI.as_view(), name="projects_api"),
    path("api/<int:pk>/", views.ProjectDetailAPI.as_view(), name="project_api_detail"),
    path("<slug:slug>/", views.project_detail, name="project_detail"),
]
