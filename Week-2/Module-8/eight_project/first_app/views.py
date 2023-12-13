from django.shortcuts import render, redirect
from . forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signUp(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            # messages.warning(request, 'Warning')
            # messages.info(request, 'info')
            print(form.cleaned_data)
            form.save()
    else:
        form = RegisterForm()
    return render(request, './signup.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username = name, password = userpass) # to check user valid or Not and user exist in databse or not
            if user is not None:
                login(request, user)
                return redirect('profile_page')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
            


def profile(request):
    return render(request, 'profile.html')

