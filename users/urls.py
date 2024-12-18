from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
        path("accounts/", include("django.contrib.auth.urls")), 
        path("accounts/register", views.register, name="register"), 
        path("accounts/profile/", views.dashboard, name="dashboard"), 
        path("accounts/login", views.user_login, name="login"),

        ]
