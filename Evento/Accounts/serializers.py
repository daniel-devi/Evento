from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed user information including sensitive fields.
    This serializer is used for displaying and interacting with user data.
    """
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "date_joined"]
        extra_kwargs = {
            "password": {"write_only": True},  # Ensure password is write-only for security
            "date_joined": {"read_only": True}  # Prevent modification of auto-generated date_joined field
        }

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.
        Hashes the password before saving the user.
        """
        return User.objects.create_user(**validated_data)

class UsernameSerializer(serializers.ModelSerializer):
    """
    Serializer for user usernames only. This is useful for operations where 
    only the username is needed, like username-based queries.
    """
    class Meta:
        model = User
        fields = ['username']

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user profiles. It includes validations for email uniqueness.
    """
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }

    def validate_email(self, value):
        """
        Validate that the email is unique across all users.
        Raises a validation error if the email is already in use by another user.
        """
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        """
        Update the user instance with the provided validated data.
        Updates first name, last name, and email fields.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UserProfileModelSerializer(serializers.ModelSerializer):
    """
    Serializer for UserProfile model.
    """
    class Meta:
        model = UserProfile
        fields = '__all__'