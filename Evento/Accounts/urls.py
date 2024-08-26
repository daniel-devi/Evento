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
    # Creates User using the Generic Create Username View
    queryset = User.objects.all() 
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]