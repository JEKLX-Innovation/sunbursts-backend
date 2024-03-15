"""
Defines the administration interface for CustomUser model in Django admin.

This module registers the CustomUser model with the Django admin site and configures
the CustomUserAdmin class to customize its appearance and behavior in the admin interface.

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Customizes the appearance and behavior of the CustomUser model in the Django admin interface.

    Attributes:
        add_form (CustomUserCreationForm): Form used for adding new CustomUser instances.
        form (CustomUserChangeForm): Form used for editing existing CustomUser instances.
        model (CustomUser): Model class being administered.
        list_display (list): List of fields displayed in the admin interface.
    """
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
