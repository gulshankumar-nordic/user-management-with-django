from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import SignUpForm, EditProfileForm
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


def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, ('Profile updated Successfully'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'userauthapp/edit-profile.html', context)


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Password updated Successfully'))
            return redirect('home')
    else:

        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'userauthapp/change-password.html', context)
