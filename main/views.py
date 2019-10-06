from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):

    context = {
        
        "body": "Body: HELLO WORLD!!!"
    }   

    return render(request, 'main/home.html', context)

def aboutpage(request):
    context = {
        "title": "About",
        "body": "Body: About ME!!!"
    }    
    return render(request, 'main/about.html', context)

def contactpage(request):
    context = {
        "title": "Contact",
        "body": "Body: How to Contact ME",
        "content": "732 or 201"
    }
    return render(request, 'main/contact.html', context)

def resumepage(request):
    context = {
        "title": "Resume",
        "body": "Body: My resume"
    }
    return render(request, 'main/resume.html', context)

def register(request):
    context = {
        "title": "Register",
        "body": "Body: Registrationg Form"
    }
    return render(request, 'main/register.html', context)

def login(request):
    context = {
        "title": "Login",
        "body": "Body: Login Form"
    }
    return render(request, 'main/login.html', context)

def logout(request):
    context = {
        "title": "Logout",
        "body": "Body: Logout and Redirect to Home Page"
    }
    return render(request, 'main/logout.html', context)

def temppage(request):
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page"
    }
    return render(request, 'main/temp.html', context)