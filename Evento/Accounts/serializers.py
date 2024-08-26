from django.contrib.auth.models import User
# Accounts
# Restframework
from rest_framework import serializers


#? Create Your Serializer

# Serializer for User Model: Serializes user data for API responses and requests
class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed user information including sensitive fields.
    This serializer is used for displaying and interacting with user data.
    """
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "date_joined"]
        extra_kwargs = {
            "password": {"write_only": True},  # Password should be write-only
            "date_joined": {"read_only": True}  # Date joined should be read-only
        }

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.
        Hashes the password before saving the user.
        """
        # Creating a user with hashed password
        user = User.objects.create_user(**validated_data)
        return user

