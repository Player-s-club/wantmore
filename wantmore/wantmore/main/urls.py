from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    # path('SignIn', views.SignIn, name='signin'),
    # path('SignUp', views.SignUp, name='signup'),
    path('profile', views.profile, name='profile'),
    path('index2', views.index2, name='index2'),
    path('logout', views.exit, name='logout'),
    path('login_or_register', views.login_or_register, name='login_or_register'),
    # path('register', views.login_or_register, name='register'),
]