from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):

    context = {
        "title": "Code Adventure",
        "body": "HELLO WORLD!!!"
    }
    

    return render(request, 'base.html', context)

def aboutpage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> About Page")

def contactpage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> Contact Page")

def resumepage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> Resume Page")