from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver


class AdvisorUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    advisor_phone_number = models.CharField("Advisor Phone Number", max_length=256, blank=False)
    role = models.CharField("Role", max_length=256)


@receiver(post_save, sender=User)
def create_advisor_user(sender, instance, created, **kwargs):
    if created:
        AdvisorUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_advisor_user(sender, instance, created, **kwargs):
    instance.advisoruser.save()
    # needs a role, advisor, volunteer, vendor, judge, workshop teacher.



# Create your models here.
