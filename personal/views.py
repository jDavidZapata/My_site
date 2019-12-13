from django.shortcuts import render, get_list_or_404
from django.http import Http404

from blog.models import Post, Category

# Create your views here.



def personal_page(request):

    personal = True
    template_name = 'personal/personal.html'
    posts = None
    try:
        #posts = Post.objects.all() #--> Query set
        categories = Category.objects.all() #--> Query set
    except ValueError:
        raise Http404
    #posts = get_list_or_404(Post, category=category)
    ordering = ['-date_posted']
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal,
        'categories': categories,
        #"posts": posts
    }
    return render(request, template_name, context)



'''
def personal_page(request):

    personal = True
    template_name = 'personal/personal.html'
    #posts = get_list_or_404(Post)
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal,
        #"posts": posts
    }
    return render(request, template_name, context)
'''

def temppage(request):

    personal = True
    template_name = 'personal/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal
    }
    return render(request, template_name, context)
