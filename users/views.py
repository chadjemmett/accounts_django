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
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            
            user = authenticate(
                    username=username,
                    password=raw_password

                    )
            login(request, user)
            return redirect("login")
    else:
        form = AdvisorCreationForm(request.POST)
        return render(request, 'registration/register.html', {"form": form })

