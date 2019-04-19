from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Hello There this is <strong>Daves's</strong> Home Page")