from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm

# Create your views here.

def register(request):

    template_name = 'users/register.html'
    if request.method == 'POST':
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
                
    form = CreateUserForm()
    context = {
        "title": "Register",
        "body": "Body: Registrationg Form",
        "form": form
    }
    return render(request, template_name, context)