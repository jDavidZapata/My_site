from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.projects_list, name="projects_list"),
    path("<int:project_id>/", views.project_detail, name="project_detail"),
    path("create/", views.project_create, name="project_create"),
    path("<int:project_id>/update/", views.project_update, name="project_update"),
    path("<int:project_id>/delete/", views.project_delete, name="project_delete"),
]