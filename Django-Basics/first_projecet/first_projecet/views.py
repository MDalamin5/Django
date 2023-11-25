from django.http import HttpResponse

def home(request):
    return HttpResponse("<h3>Assalamualikum, Wellcome to Our Home Page</h3>")

def about(request):
    return HttpResponse("Hello! Its Our About Page.")