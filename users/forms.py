from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, AuthenticationForm
from . models import AdvisorUser
from django import forms






class AdvisorCreationForm(UserCreationForm):
    email = forms.EmailField()
    advisor_phone_number = forms.CharField(label="Contact Number", max_length=255)
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)



class AdvisorLoginForm(AuthenticationForm):
    pass
