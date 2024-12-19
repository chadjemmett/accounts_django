from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from . forms import AdvisorCreationForm, AdvisorLoginForm
from django.contrib.auth.models import User
from . models import AdvisorUser

# Create your views here

def register(request):
    if request.method == "POST":
        form = AdvisorCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("advisor_phone_number")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            
            User.objects.create_user(
                    username=username,
                    password=raw_password,
                    email=email,
                    advisoruser=AdvisorUser(advisor_phone_number=phone),
                    first_name=first_name,
                    last_name=last_name,
                    )
            
            return redirect("dashboard")
    else:
        form = AdvisorCreationForm(request.POST)
        return render(request, 'registration/register.html', {"form": form })





def user_logout(request):
    logout(request)
    return render(requests, "login.html")

# needs a login page to redirect to.
@login_required()
def dashboard(request):
    #show the options to access here. For students. For Teams etc. This is for Advisors
    return render(request, "dashboard.html")



