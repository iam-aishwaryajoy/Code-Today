from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='home'),
    path('home/',home,name='home'),
    path('login-h/', loginpage, name="login-h"),
    path('register/', register, name="register"),
    path('logout-h/', logoutUser, name="logout-h"),
    path('photo/',photo,name='photo'),
]
