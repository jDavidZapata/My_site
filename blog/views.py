from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category, Comment
from .forms import PostForm, PostModelForm, CategoryModelForm

# Create your views here.



def category_list(request):

    personal = True
    template_name = 'blog/category_list.html'
    categories = get_list_or_404(Category)
    ordering = ['name']
    #categories = Category.objects.all() #--> Query set
    context = {
            'title': '* Categories *',
            'categories': categories,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)



class CategoryListView(ListView):

    personal = True
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'
    ordering = ['-date_added']




def category_detail_list(request, cat_id):

    personal = True
    template_name = 'blog/category_detail.html'
    categories = get_list_or_404(Category)
    category = get_object_or_404(Category, pk=cat_id)
    posts = get_list_or_404(Post, category=category)
    ordering = ['-date_posted']
    #posts = Post.objects.all() #--> Query set
    context = {
            'title': '*Category Posts *',
            'categories': categories,
            'category': category,
            'posts': posts,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)




class CategoryDetailListView(ListView):

    personal = True
    model = Post
    template_name = 'blog/category_detail.html'
    context_object_name = 'posts'
    ordering = ['-date_added']



@login_required
def category_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data)
            ##category = Category.objects.create(**form.cleaned_data)
            category = form.save(commit=False)
            category.author = request.user
            category.save()
            messages.success(request, f"New Category Created: {category.name}.")
            return redirect(category)
        else:
            messages.error(request, "Invalid Create")
    form = CategoryModelForm()
    context = {
            'title': 'Create A Category',
            'form': form 
        }
    return render(request, template_name, context)



class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



@login_required
def category_delete(request, cat_id):
    category = get_object_or_404(Post, pk=cat_id)
    template_name = 'blog/delete.html'
    print(request.POST)
    if request.method == 'POST':
        if category.author == request.user:            
            category.delete()
            messages.success(request, f"Category Deleted.")
            return redirect('blog:posts_list') 
        else:
            messages.error(request, "Invalid Delete")
    context = {
        'title': f'Delete Category {category.name}',
        'post': category 
    }
    return render(request, template_name, context)



def posts_list(request):

    personal = True
    template_name = 'blog/posts_list.html'
    posts = get_list_or_404(Post)
    ordering = ['-date_posted']
    #posts = Post.objects.all() #--> Query set
    context = {
            'title': '* Posts *',
            'posts': posts,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)



class PostListView(ListView):

    personal = True
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']




def post_detail(request, post_id):

    personal = True
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)   
    context = {
            'title': f'Post # {post_id}',
            'post': post,
            'personal': personal
        }        
    return render(request, template_name, context)



class PostDetailView(DetailView):

    personal = True
    model = Post
    template_name = 'blog/post_detail.html'



@login_required
def post_create(request):
    
    template_name = 'form.html'
    print(request.POST)
    if request.method == 'POST':
        form = PostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form.cleaned_data)
            ##post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.author = request.user
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



class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template_name = 'form.html'
    if request.method == 'POST':
        form = PostModelForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid() and post.author == request.user:
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
    template_name = 'blog/delete.html'
    print(request.POST)
    if request.method == 'POST':
        if post.author == request.user:            
            post.delete()
            messages.success(request, f"Post Deleted.")
            return redirect('blog:posts_list') 
        else:
            messages.error(request, "Invalid Delete")
    context = {
        'title': f'Delete Post {post.title}',
        'post': post 
    }
    return render(request, template_name, context)


'''
def post_detail(request, slug):

    personal = True
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)   
    context = {
            'title': f'Post # {post.id}',
            'personal': personal,
            'post': post
        }        
    return render(request, template_name, context)



def category_detail_list(request, slug):

    personal = True
    template_name = 'blog/category_detail.html'
    category = get_object_or_404(Category, slug)
    posts = get_list_or_404(Post, category=category)
    ordering = ['date_posted']
    #posts = Post.objects.all() #--> Query set
    context = {
            'title': '*Category Posts *',
            'category': category,
            'posts': posts,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)

'''