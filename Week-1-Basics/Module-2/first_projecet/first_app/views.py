from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is new home page')

def about(request):
    return HttpResponse('This is our about page from first app')
