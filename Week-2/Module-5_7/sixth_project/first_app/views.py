from django.shortcuts import render, redirect
from . import models
# Create your views here.

def home(request):
    student = models.Student.objects.all()
    return render(request, 'index.html', {'data' : student})


def delete_student(request, roll):
    stu = models.Student.objects.get(pk = roll).delete()
    
    student = models.Student.objects.all()
    return redirect("homepage")
