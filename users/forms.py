from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . models import AdvisorUser
from django import forms






class AdvisorCreationForm(UserCreationForm):
    email = forms.EmailField()
    advisor_phone_number = forms.CharField(label="Contact Number", max_length=255)

    # class Meta:
    #    model = AdvisorUser
    #    fields = ("advisor_phone_number",)
