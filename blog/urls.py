from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    #path("<slug:slug>/", views.post_detail, name="post_detail"),
    #path("blog-post/", post_create, name="post_create"),
    path("<int:post_id>/update/", views.post_update, name="post_update"),
    path("<int:post_id>/delete/", views.post_delete, name="post_delete"),
]