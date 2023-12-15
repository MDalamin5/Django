from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name="homepage"),
    path('', views.set_session, name="homepage"),
    # path('get/', views.get_cooki),
    path('get/', views.get_session),
    # path('del/', views.del_cooki),
    path('del/', views.delete_Session),
]
