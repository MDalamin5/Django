from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('get/', views.get_cooki),
    path('del/', views.del_cooki),
]
