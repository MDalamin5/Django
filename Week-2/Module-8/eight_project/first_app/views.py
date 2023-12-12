from django.shortcuts import render
from . forms import RegisterForm

# Create your views here.

def home(request):
    form = RegisterForm()
    return render(request, 'index.html', {'form' : form})
