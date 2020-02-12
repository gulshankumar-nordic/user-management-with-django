from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import SignUpForm
# Create your views here.


def home(request):
    return render(request, 'userauthapp/home.html', {})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Successfully logged in'))
            return redirect('home')
        else:
            messages.success(request, ('Error! Please try again'))
            return redirect('login')
    else:
        return render(request, 'userauthapp/login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, ('Successfully logged out'))
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Successfully Registered'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'userauthapp/register.html', context)
