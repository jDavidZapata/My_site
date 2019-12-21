from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .models import Post, Category, Comment
from .forms import PostForm, PostModelForm, CategoryModelForm

# Create your views here.


class CategoryListView(ListView):

    personal = True
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'
    #paginate_by = 3
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['personal'] = True       
        return context


class CategoryDetailListView(ListView):

    template_name = 'blog/category_detail.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category).order_by('-date_posted')
    

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailListView, self).get_context_data(**kwargs)
        context['personal'] = True       
        context['category'] = self.category
        context['categories'] = Category.objects.order_by('name')
        return context


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'form.html'
    fields = ['name', 'summary']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CategoryDelete(DeleteView):
    model = Category
    template_name = 'blog/category_delete.html'
    success_url = reverse_lazy('blog:category_list')






class PostListView(ListView):

    personal = True
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'
    #paginate_by = 2
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['personal'] = True       
        return context


class PostDetailView(DetailView):

    personal = True
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['personal'] = True       
        return context
    
    
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'form.html'
    #form_class = PostModelForm
    fields = ['title', 'content', 'category', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'form.html'
    fields = ['title', 'content', 'category', 'image']


@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:posts_list')





'''
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



def category_detail_list(request, cat_id):

    personal = True
    template_name = 'blog/category_detail.html'
    categories = get_list_or_404(Category)
    category = get_object_or_404(Category, pk=cat_id)
    posts = get_list_or_404(Post, category=category)
    ordering = ['-date_posted']
    #posts = Post.objects.all() #--> Query set
    context = {
            'title': f'* {category.name} Category Posts *',
            'categories': categories,
            'category': category,
            'posts': posts,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)
'''


def category_list(request):

    personal = True
    template_name = 'blog/category_list.html'
    #categories = get_list_or_404(Category)
    ordering = ['-date_added']
    categories = None
    try:
        categories = Category.objects.all() #--> Query set
    except ValueError:
        raise Http404
    context = {
            'title': '* Categories *',
            'categories': categories,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)


def category_detail_list(request, slug):

    personal = True
    template_name = 'blog/category_detail.html'
    categories = get_list_or_404(Category)
    category = get_object_or_404(Category, slug=slug)
    posts = None
    try:
        posts = Post.objects.filter(category=category) #--> Query set
    except ValueError:
        raise Http404
    #posts = get_list_or_404(Post, category=category)
    ordering = ['-date_posted']
    #posts = Post.objects.all() #--> Query set
    context = {
            'title': f'* {category.name} Category Posts *',
            'categories': categories,
            'category': category,
            'posts': posts,
            'personal': personal,
            'ordering': ordering
        }

    return render(request, template_name, context)





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


@login_required
def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    template_name = 'blog/category_delete.html'
    print(request.POST)
    if request.method == 'POST':
        if category.author == request.user:            
            category.delete()
            messages.success(request, f"Category Deleted.")
            return redirect('blog:category_list') 
        else:
            messages.error(request, "Invalid Delete")
    context = {
        'title': f'Delete Category {category.name}',
        'category': category 
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


def post_detail(request, slug):

    personal = True
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)   
    context = {
            'title': f'Post # {post.id}',
            'post': post,
            'personal': personal
        }        
    return render(request, template_name, context)


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
            post.category = Category.objects.get(pk=request.POST['category'])
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
def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
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
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template_name = 'blog/post_delete.html'
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