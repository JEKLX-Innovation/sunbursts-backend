"""
Defines URL patterns for the 'accounts' app in Django.

This module specifies the URL patterns for the 'accounts' app, including the path for the sign-up view.

"""

from django.urls import path

from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
