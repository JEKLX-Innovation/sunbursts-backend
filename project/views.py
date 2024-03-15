"""
Defines custom token serializers and views for token obtainment in Django Rest Framework.

This module provides the MyTokenObtainPairSerializer and MyTokenObtainPairView classes,
which customize the token serialization and token obtainment process.

"""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for obtaining token pairs.

    Inherits from TokenObtainPairSerializer.

    Methods:
        get_token(cls, user): Customizes token generation by adding custom claims.

    """

    @classmethod
    def get_token(cls, user):
        """
        Customizes token generation by adding custom claims.

        Args:
            user: User instance for which the token is generated.

        Returns:
            token: Generated token with custom claims.

        """
        token = super().get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["username"] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Custom view for obtaining token pairs.

    Inherits from TokenObtainPairView.

    Attributes:
        serializer_class (MyTokenObtainPairSerializer): Custom serializer class for token obtainment.

    """
    serializer_class = MyTokenObtainPairSerializer
