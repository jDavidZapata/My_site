from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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
    if request.method == 'POST':

        form = ContactForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            messages.info(request, f"Your message has been sended.")
            return redirect('main:homepage')
        else:
            messages.error(request, "Invalid Form.")
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        
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


def temppage(request):

    personal = True
    template_name = 'main/temp.html'
    context = {
        "title": "Temporary",
        "body": "Body: Temp Page",
        "personal0": "True"
    }
    return render(request, template_name, context)
