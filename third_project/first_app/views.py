from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html' , context= {'author': 'Md Al Amin', 'age':24,'mark': 79})
