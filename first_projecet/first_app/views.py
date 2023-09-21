from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello Sir!! Its my First Django Page <h2>Allhamdulilla</h2>")

def about(request):
    return HttpResponse ("Its my about page")
