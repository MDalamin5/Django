from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("its courses Page")

def fidback(request):
    return HttpResponse("This is our Fidback Page")
