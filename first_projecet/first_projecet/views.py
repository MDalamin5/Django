from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Sir!! Its my First Django Page <h2>Allhamdulilla</h2>")

def about(request):
    return HttpResponse ("Its my about page")

def alamin(request):
    return HttpResponse ("Its My Portfollio")