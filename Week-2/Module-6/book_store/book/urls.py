from django.urls import path
from . import views
# from book.views import home, store_book, show_books, edit_book, delete_book

urlpatterns = [
    # path('',views.home, name="homepage"),
    # path('',views.TemplateView.as_view(template_name = 'home.html')),
    path('<int:roll>/', views.MyTemplateHomeView.as_view(), {'author' : 'rahim'}, name='homepage'),
    path('store_book/', views.store_book, name='storebook'),
    path('show_book/', views.show_books, name='show_books'),
    path('edit_book/<int:id>', views.edit_book, name="edit_book" ),
    path('delete_book/<int:id>', views.delete_book, name="delete_book")
]
