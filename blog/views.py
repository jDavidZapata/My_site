from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from .models import Post
#from .forms import PostForm, PostModelForm

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

'''
@login_required
def post_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    if request.method == 'POST':
        form = PostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, f"New Post Created: {post.title}.")
            return redirect(post)
        else:
            messages.error(request, "Invalid Create")
    form = PostModelForm()
    context = {
            'title': 'Create A Post',
            'form': form 
        }
    return render(request, template_name, context)



@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template_name = 'form.html'
    if request.method == 'POST':
        form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid() and post.user == request.user:
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.save() 
            messages.success(request, f"{post.title}: Post Updated.")
            return redirect(post)
        else:
            messages.error(request, "Invalid Update")
    
    form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
    context = {
        'title': f'Update Post {post.title}',
        'form': form 
    }
    return render(request, template_name, context)



@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template_name = 'form.html'
    print(request.POST)
    if request.method == 'POST':
        form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid() and post.user == request.user:
            print(form.cleaned_data)             
            post.delete()
            messages.success(request, f"Post Deleted.")
            return redirect('blog:posts_list') 
        else:
            messages.error(request, "Invalid Delete")
    form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
    context = {
        'title': f'Delete Post {post.title}',
        'form': form 
    }
    return render(request, template_name, context)
'''