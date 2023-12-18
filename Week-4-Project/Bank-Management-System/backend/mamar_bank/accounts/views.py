from django.shortcuts import render
from django.views.generic import FormView
from . forms import UserRegistrationsForm
from django.contrib.auth import login

# Create your views here.

class UserRegistrationView(FormView):
    template_name = ''
    form_class = UserRegistrationsForm
    success_url = ''
    
    def form_valid(self, form):
        user = form.save()
        login(user)
        return super().form_valid(form) # there form_valid function call autometicly if the form is valid data