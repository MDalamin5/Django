from django.shortcuts import render

# Create your views here.

def feedback(request):
    return render(request, './first_app/index.html', {'name' : 'Md Al Amin', 'age' : 23})
