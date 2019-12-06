from django.shortcuts import render, get_list_or_404
from blog.models import Post

# Create your views here.


def personal_page(request):

    personal = True
    template_name = 'personal/personal.html'
    posts = get_list_or_404(Post)
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal,
        "posts": posts
    }
    return render(request, template_name, context)


def temppage(request):

    personal = True
    template_name = 'personal/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal": personal
    }
    return render(request, template_name, context)
