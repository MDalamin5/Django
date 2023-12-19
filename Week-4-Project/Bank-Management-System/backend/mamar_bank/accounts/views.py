from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from . forms import UserRegistrationsForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class UserRegistrationView(FormView):
    template_name = './accounts/user_registration.html'
    form_class = UserRegistrationsForm
    success_url = reverse_lazy('register')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form) # there form_valid function call autometicly if the form is valid data
    
    
class UserLoginView(LoginView):
    template_name = './accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    
        