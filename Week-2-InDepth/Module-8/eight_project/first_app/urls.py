from django.urls import path
from first_app.views import home, signUp, profile, user_login, user_logout, pass_change, pass_change2

urlpatterns = [
    path('',home, name='homepage'),
    path('signup/', signUp, name="signup"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name="profile_page"),
    path('pass_change/', pass_change, name="pass_change"),
    path('pass_change2/', pass_change2, name="pass_change2"),
    
]
