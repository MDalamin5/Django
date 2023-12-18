from django.urls import path
from . import views
# from book.views import home, store_book, show_books, edit_book, delete_book

urlpatterns = [
    # path('',views.home, name="homepage"),
    # path('',views.TemplateView.as_view(template_name = 'home.html')),
    # path('<int:roll>/', views.MyTemplateHomeView.as_view(), {'author' : 'rahim'}, name='homepage'),
    path('', views.MyTemplateHomeView.as_view(), {'author' : 'rahim'}, name='homepage'),
    # path('store_book/', views.store_book, name='storebook'),
    path('store_book/', views.BookFormView.as_view(), name='storebook'),
    # path('show_book/', views.show_books, name='show_books'),
    path('show_book/', views.BookListViwe.as_view(), name='show_books'),
    path('book_datails/<int:id>', views.BookDatailsView.as_view(), name='book_datails'),
    # path('edit_book/<int:id>', views.edit_book, name="edit_book" ),
    path('edit_book/<int:pk>', views.BookUpdateView.as_view(), name="edit_book" ),
    # path('delete_book/<int:id>', views.delete_book, name="delete_book")
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name="delete_book")
]
