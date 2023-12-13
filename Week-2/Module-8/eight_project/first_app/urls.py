from django.urls import path
from first_app.views import home, signUp, profile

urlpatterns = [
    path('',home, name='homepage'),
    path('signup/', signUp, name="signup"),
    path('profile/', profile, name="profile_page"),
]
