from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's AbstractUser.

    Add any additional fields or methods here as needed.
    """
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
