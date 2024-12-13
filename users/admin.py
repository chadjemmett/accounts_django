from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import AdvisorUser
from django.contrib.auth.models import User

class AdvisorUserAdmin(admin.StackedInline):
    model = AdvisorUser


class UserAdmin(BaseUserAdmin):
    inlines = [AdvisorUserAdmin]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)



# Register your models here.
