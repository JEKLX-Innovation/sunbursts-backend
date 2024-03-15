"""
Defines the configuration for the 'accounts' app in Django.

This module specifies the configuration for the 'accounts' app, including its name.

"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration class for the 'accounts' app.

    Attributes:
        name (str): Name of the app.
    """
    name = "accounts"
