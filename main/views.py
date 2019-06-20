from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):

    context = {
        
        "body": "HELLO WORLD!!!"
    }   

    return render(request, 'main/home.html', context)

def aboutpage(request):
    context = {
        "title": "About",
        "body": "About ME!!!"
    }    
    return render(request, 'main/about.html', context)

def contactpage(request):
    context = {
        "title": "Contact",
        "body": "How to Contact ME"
    }
    return render(request, 'main/contact.html', context)

def resumepage(request):
    context = {
        "title": "Resume",
        "body": "My resume"
    }
    return render(request, 'main/resume.html', context)

def register(request):
    context = {
        "title": "Register",
        "body": "Registrationg Form"
    }
    return render(request, 'main/register.html', context)

def login(request):
    context = {
        "title": "Login",
        "body": "Login Form"
    }
    return render(request, 'main/login.html', context)

def logout(request):
    context = {
        "title": "Logout",
        "body": "Logout and Redirect to Home Page"
    }
    return render(request, 'main/logout.html', context)