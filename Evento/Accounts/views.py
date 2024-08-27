from django.conf import settings
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
# Accounts
from .models import *
from .serializers import *
# Restframework
from rest_framework import generics 
from rest_framework import views 
from rest_framework.permissions import *


# Create your views here.

class CreateUserView(generics.CreateAPIView): 
    """
    Creates a new user using the Generic CreateAPIView.
    This view allows any user (authenticated or not) to create a new account.
    """
    queryset = User.objects.all() 
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

class UserDetailByEmailView(generics.ListAPIView):
    """
    Retrieve a list of users based on their email address using the Generic ListView.
    This view allows querying users by their email address.
    """
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Filter users by email based on the `email` URL parameter.
        """
        email = self.kwargs['email']
        return User.objects.filter(email=email)

class UserListViewByUsername(generics.ListAPIView):
    """
    Retrieve a list of all users with only their usernames.
    This view provides a list of all users in the system, showing only their usernames.
    """
    serializer_class = UsernameSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]