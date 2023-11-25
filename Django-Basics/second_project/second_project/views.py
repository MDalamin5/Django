from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Our home page create from Parent project")