from django.shortcuts import render, redirect
from first_app.forms import TaskStoreForm
from first_app.models import TaskMode
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class MyTemplateHomeView(TemplateView):
    template_name = 'home.html'



def store_task(request):
    if request.method == 'POST':
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('show_tasks')
    else:
        task = TaskStoreForm()
    return render(request, 'store_task.html', {'form' : task})

def show_tasks(request):
    task = TaskMode.objects.filter(is_completed=False)
    return render(request, 'show_tasks.html', {'tasklist' : task})


class TaskUpdateView(UpdateView):
    model = TaskMode
    template_name = 'store_task.html'
    form_class = TaskStoreForm
    success_url = reverse_lazy('show_tasks')

def delete_task(request, id):
    task = TaskMode.objects.get(pk = id).delete()
    return redirect('show_tasks')




def complete_tasks(request, id):
    if id:
        task = TaskMode.objects.get(pk=id)
        task.is_completed = True
        task.save()

    task = TaskMode.objects.filter(is_completed=True)
    return render(request, 'complete_tasks.html', {'tasklist' : task})
    
    


def show_com_tasks(request):
    task = TaskMode.objects.filter(is_completed=True)
    return render(request, 'complete_tasks.html', {'tasklist' : task})







