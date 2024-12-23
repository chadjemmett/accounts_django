from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
        path("accounts/", include("django.contrib.auth.urls")), 
        path("accounts/register", views.register, name="register"), 
        path("accounts/profile/", views.dashboard, name="dashboard"), 
        path("accounts/login", auth_views.LoginView.as_view(), name="login"),
        path("accounts/logout", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout",),
        path("accounts/password-reset",
        auth_views.PasswordResetView.as_view(template_name="registration/password-reset.html"),
        name="password-reset")
        ]
