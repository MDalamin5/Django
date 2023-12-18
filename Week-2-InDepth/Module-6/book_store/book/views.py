from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
# function Base view
# def home(request):
#     return render(request, 'home.html')

"""
Function Base Viwe

"""

class MyTemplateHomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name' : 'Md Al AMin', 'age' : 23}
        print(context)
        context.update(**kwargs)
        print(context)
        return context








# def store_book(request):
#     if request.method == "POST":
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('show_books')
#     else:
#         book = BookStoreForm()
#     return render(request, 'store_book.html', {'form' : book})
    
# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     success_url = reverse_lazy('show_books')

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('show_books')
    
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')
    




# function base view
# def show_books(request):
#     book = BookStoreModel.objects.all()
#     return render(request, 'show_book.html', {'data' : book})


# Class Base views

class BookListViwe(ListView):
    model = BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'booklist'

    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author='Python')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = {'booklist' : BookStoreModel.objects.order_by('author')} #ordering
    #     return context
    
    # ordering = ['category']
    ordering = ['-id']


    # Home Work
    """def get_template_names(self):
        if self.request.user.is_superuser:
            template_name = 'superuser.html'
        elif self.request.user.is_staff:
            template_name = 'staf.html'
        else:
            self.template_name
        return [template_name]"""
    

class BookDatailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_datails.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
        

    


# def edit_book(request, id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance = book)
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST, instance = book)
#         if book.is_valid():
#             book.save()
#             return redirect('show_books')
#     return render(request, 'store_book.html', {'form' : form})


# class based View

class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('show_books')


class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'del_confo.html'
    success_url = reverse_lazy('show_books')


# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk = id).delete()
#     return redirect('show_books')

