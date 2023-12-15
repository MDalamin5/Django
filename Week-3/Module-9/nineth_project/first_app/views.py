from django.shortcuts import render

# Create your views here.

def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'Md Al Amin')
    response.set_cookie('Uni', 'NSU')
    return response

def get_cooki(request):
    name = request.COOKIES.get('name')
    return render(request, 'get.html', {'name' : name})



def del_cooki(request):
    pass

