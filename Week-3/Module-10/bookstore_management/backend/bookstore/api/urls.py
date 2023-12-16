from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
# router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('books/', views.BookListView.as_view()), # get and post request handel
    # path('books/<int:pk>/', views.BookListUpdateDelete.as_view()), # 
    # path('books/', views.BookListCreateAPIView.as_view()), # get and post request handel
    # path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()), # update and delete
    path('', include(router.urls)),
]