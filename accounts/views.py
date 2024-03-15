"""
Defines a sign-up view using Django's generic CreateView.

This module provides the SignUpView class, which is a generic CreateView for signing up users.
It uses the CustomUserCreationForm for user input and redirects to the login page upon successful sign-up.

"""

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    """
    View for user sign-up.

    Inherits from Django's CreateView.

    Attributes:
        form_class (CustomUserCreationForm): Form class for user input.
        success_url (str): URL to redirect to upon successful sign-up.
        template_name (str): Name of the template used for rendering the sign-up page.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"