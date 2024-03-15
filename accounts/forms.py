"""
Defines custom forms for creating and changing CustomUser instances in Django.

This module provides CustomUserCreationForm and CustomUserChangeForm, which are subclasses
of Django's UserCreationForm and UserChangeForm. These custom forms are tailored
to work with the CustomUser model.

"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Form for creating a new CustomUser instance.

    Inherits from Django's UserCreationForm.

    Attributes:
        Meta: Configuration class specifying model and fields.
    """

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """
    Form for changing an existing CustomUser instance.

    Inherits from Django's UserChangeForm.

    Attributes:
        Meta: Configuration class specifying model and fields.
    """
    class Meta:
        model = CustomUser
        fields = ("username", "email")
