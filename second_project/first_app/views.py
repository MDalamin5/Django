from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse("This contact page")

def about(request):
    return HttpResponse("This about page")
