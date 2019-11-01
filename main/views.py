from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import ContactForm, CreateUserForm


# Create your views here.

def homepage(request):

    template_name = 'main/home.html'
    context = {        
        "body": "Body: HELLO WORLD!!!"
    }   
    return render(request, template_name, context)

def aboutpage(request):

    template_name = 'main/about.html'
    context = {
        "title": "About",
        "body": "Body: About ME!!!"
    }    
    return render(request, template_name, context)

def contactpage(request):

    template_name = 'main/contact.html'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact",
        "body": "Body: How to Contact ME",
        "content": "732 or 201",
        "form": form
    }
    return render(request, template_name, context)

def resumepage(request):

    template_name = 'main/resume.html'
    context = {
        "title": "Resume",
        "body": "Body: My resume"
    }
    return render(request, template_name, context)

def register(request):

    template_name = 'main/signup.html'
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        user = form.save()
        print(f"request ===== >{request}")
        print(f"user ===== >{user}")
        login(request, user)
        return redirect('main:homepage')

    context = {
        "title": "Register",
        "body": "Body: Registrationg Form",
        "form": form
    }
    return render(request, template_name, context)

'''
def login(request):

    template_name = 'main/login.html'
    context = {
        "title": "Login",
        "body": "Body: Login Form"
    }
    return render(request, template_name, context)

def logout(request):

    template_name = 'main/logout.html'
    context = {
        "title": "Logout",
        "body": "Body: Logout and Redirect to Home Page"
    }
    return render(request, template_name, context)
'''

def temppage(request):

    template_name = 'main/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page"
    }
    return render(request, template_name, context)