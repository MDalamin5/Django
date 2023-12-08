from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, './f_app/home.html')


def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './f_app/about.html', {'name' : name, 'email' : email, 'select' : select})
    else:
        return render(request, './f_app/about.html')


def submit_form(request):
    return render(request, './f_app/form.html')