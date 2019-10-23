from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

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
    print(request.POST)
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

    template_name = 'main/register.html'
    context = {
        "title": "Register",
        "body": "Body: Registrationg Form"
    }
    return render(request, template_name, context)

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

def temppage(request):

    template_name = 'main/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page"
    }
    return render(request, template_name, context)