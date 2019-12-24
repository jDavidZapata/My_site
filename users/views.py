from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CreateUserForm, UpdateUserForm, UpdateProfileForm
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
            return redirect('personal:personal')
        else:
            messages.error(request, "Invalid Registration")
    form = CreateUserForm()
    context = {
        "title": "Register",
        "body": "Body: Registrationg Form",
        "form": form,
        "personal": True,
    }
    return render(request, template_name, context)


@login_required
def profile(request):

    template_name = 'users/profile.html'
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST or None, instance=request.user)
        profile_form = UpdateProfileForm(request.POST or None, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your Account has been updated!")
            return redirect('users:profile')
        else:
            messages.error(request, "Invalid Update")
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        "title": "Profile",
        "user_form": user_form,
        "profile_form": profile_form
    }    
    return render(request, template_name, context)


def login_(request):

    personal = True
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
        
    form = AuthenticationForm()
    context = {
        "title": "Login",
        "body": "Body: Login Form",
        "form": form,
        "next": redirect_to,
        "personal": personal
    }
    return render(request, template_name, context)


@login_required
def logout_(request):

    redirect_to = request.POST.get('next', request.GET.get('next', '/'))
    redirect_to = (redirect_to
                   if http.is_safe_url(redirect_to, request.get_host())
                   else '/')
    logout(request)
    messages.info(request, f"You are now logged out.")
    if redirect_to != '':
        return redirect(redirect_to)
    else:    
        return redirect('personal:personal')





class UserRegistration(CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserModelForm
