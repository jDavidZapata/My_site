from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> Home Page")

def aboutpage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> About Page")

def contactpage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> Contact Page")

def resumepage(request):
    return HttpResponse("<strong>Hello World</strong> !!! This is <strong>Daves's</strong> Resume Page")