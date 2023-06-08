from django.contrib import admin
from .models import UserModel


# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")
    filter_horizontal = ('groups', 'user_permissions')
    list_filter = ("role",)
