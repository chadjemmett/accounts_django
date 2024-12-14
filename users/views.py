from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . forms import AdvisorCreationForm
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
            
            return redirect("login")
    else:
        form = AdvisorCreationForm(request.POST)
        return render(request, 'registration/register.html', {"form": form })

