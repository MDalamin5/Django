from django.urls import path
from . import views
from first_app.views import home, show_data

urlpatterns = [
    # path('', views.home, name="homepage"),
    path('', home, name="homepage"),
    path('show_data/', show_data, name="showData")
]
