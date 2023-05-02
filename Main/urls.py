from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", home, name="home"),
    path("register", register, name="register"),
    path("login/", LoginView.as_view(template_name="Main/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="Main/logout.html"), name="logout"),
    path("register2/", frontend_register, name="register2"),
    path("login2/", frontend_login, name="login2")
]