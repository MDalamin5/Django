from django.shortcuts import render
from . forms import RegisterForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            # messages.warning(request, 'Warning')
            # messages.info(request, 'info')
            print(form.cleaned_data)
            form.save()
    else:
        form = RegisterForm()
    return render(request, 'index.html', {'form' : form})
