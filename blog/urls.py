from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    #path("", PostListView.as_view(), name="posts_list"),

    path("<int:post_id>/", views.post_detail, name="post_detail"),    
    #path("<slug:slug>/", views.post_detail, name="post_detail"),
    #path('<int:post_id>', PostDetailView.as_view(), name='post_detail'),
    #path('<slug:slug>', PostDetailView.as_view(), name='post_detail'),

    #path("blog-post/", views.post_create, name="post_create"),

    path("category/", views.category_list, name="category_list"),
    #path('category/', CategoryListView.as_view(), name='category_list'),

    path("category/<int:cat_id>/", views.category_detail_list, name="category_detail"),
    #path("category/<slug:slug>/", views.category_detail_list, name="category_detail"),
    #path('category/<int:cat_id>', CategoryDetailListView.as_view(), name='category_detail'),
    #path('category/<slug:slug>', CategoryDetailListView.as_view(), name='category_detail'),

    path("category-create/", views.category_create, name="category_create"),
    #path("category-create/", CategoryCreateView.as_view(), name="category_create"),
    
    path("category<int:cat_id>/delete/", views.category_delete, name="category_delete"),

    path("<int:post_id>/update/", views.post_update, name="post_update"),
    path("<int:post_id>/delete/", views.post_delete, name="post_delete"),

]