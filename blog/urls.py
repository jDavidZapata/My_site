from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #path("", views.posts_list, name="posts_list"),
    path("", views.PostListView.as_view(), name="posts_list"),

    #path("<int:post_id>/", views.post_detail, name="post_detail"),    
    #path("<slug:slug>/", views.post_detail, name="post_detail"),
    #path('<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),

    #path("blog-post/", views.post_create, name="post_create"),
    #path("blog-post/", views.PostCreateView.as_view(), name="post_create"),

    #path("category/", views.category_list, name="category_list"),
    path('category/', views.CategoryListView.as_view(), name='category_list'),

    #path("category/<int:cat_id>/", views.category_detail_list, name="category_detail"),
    #path("category/<slug:slug>/", views.category_detail_list, name="category_detail"),
    path('category-<slug:slug>/', views.CategoryDetailListView.as_view(), name='category_detail'),
    #path('category/<slug:slug>', CategoryDetailListView.as_view(), name='category_detail'),

    path("create-category/", views.category_create, name="category_create"),
    #path("create-category/", CategoryCreateView.as_view(), name="category_create"),
    
    path("category-<slug:slug>/delete/", views.category_delete, name="category_delete"),
    #path("category-<slug:slug>/delete/", views.CategoryDelete.as_view(), name="category_delete"),

    path("category/<slug:slug>/update/", views.post_update, name="post_update"),
    #path("category/<slug:slug>/update/", views.PostUpdateView.as_view(), name="post_update"),

    path("category/<slug:slug>/delete/", views.post_delete, name="post_delete"),
    #path("category/<slug:slug>/delete/", views.PostDelete.as_view(), name="post_delete"),

]