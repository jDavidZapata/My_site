from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
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
'''
def register(request):

    template_name = 'main/signup.html'
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        user = form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"New Account Created: Welcome {username}.")
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('main:homepage')
    else:
        for msg in form.error_messages:
            messages.error(request, f"{msg}: {form.error_messages[msg]}")

    context = {
        "title": "Register",
        "body": "Body: Registrationg Form",
        "form": form
    }
    return render(request, template_name, context)


def loginpage(request):

    template_name = 'main/login.html'
    form = AuthenticationForm(request.POST or None)
    if form.is_valid():
        user = form.get_user()
        username = form.cleaned_data.get('username')
        login(request, user=user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('main:homepage')
    else:
        for msg in form.error_messages:
            print(form.error_messages[msg])

    context = {
        "title": "Login",
        "body": "Body: Login Form"
    }
    return render(request, template_name, context)

def logoutpage(request):

    logout(request)
    messages.info(request, f"You are now logged out.")
    return redirect('main:homepage')
'''

def temppage(request):

    template_name = 'main/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page"
    }
    return render(request, template_name, context)
