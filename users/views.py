from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm
from django.utils import http

# Create your views here.

def register(request):

    template_name = 'users/register.html'
    if request.method == 'POST':
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: Welcome {username}.")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = CreateUserForm()
        context = {
            "title": "Register",
            "body": "Body: Registrationg Form",
            "form": form
        }
    return render(request, template_name, context)


@login_required
def profile(request):
    return render(request, "users/profile.html")


def login_(request):

    redirect_to = request.POST.get('next', request.GET.get('next', '/'))
    redirect_to = (redirect_to
                   if http.is_safe_url(redirect_to, request.get_host())
                   else '/')
    template_name = 'users/login.html'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST or None)
        print(request.POST)
        if form.is_valid():    
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and redirect_to == '':
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('main:homepage')
            if user is not None and redirect_to != '':
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(redirect_to)
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = AuthenticationForm()
        context = {
            "title": "Login",
            "body": "Body: Login Form",
            "form": form,
            "next": redirect_to,
        }
    return render(request, template_name, context)


@login_required
def logout_(request):

    logout(request)
    messages.info(request, f"You are now logged out.")
    return redirect('main:homepage')