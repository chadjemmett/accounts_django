from django.db import models
from django.contrib.auth.models import AbstractUser, User


class AdvisorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField("email address", unique=True)
    advisor_name = models.CharField("Advisor Name", max_length=256, blank=False)
    advisor_phone_number = models.CharField("Advisor Phone Number", max_length=256, blank=False)
    # needs a role, advisor, volunteer, vendor, judge, workshop teacher.

    def __str__(self):
        return self.advisor_name


# Create your models here.
