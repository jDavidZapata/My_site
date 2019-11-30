from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Post

# Create your views here.

def posts_list(request):

    template_name = 'blog/posts_list.html'
    posts = get_list_or_404(Post)
    context = {
            'title': '* Posts *',
            'posts': posts
        }

    return render(request, template_name, context)


def post_detail(request, post_id):

    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
   
    context = {
            'title': f'Post # {post_id}',
            'post': post
        }        
    return render(request, template_name, context)