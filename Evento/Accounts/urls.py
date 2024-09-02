from django.urls import path
from .views import *

# URL patterns for the Accounts-related views
# Base URL: localhost:8000/Accounts-api/
urlpatterns = [
    # Endpoint to retrieve a list of all users with only their usernames.
    path('get-usernames', UserListViewByUsername.as_view(), name='user-list-by-username'),

    # Endpoint to retrieve user details based on the provided email address.
    path('get-user-through-email/<str:email>/', UserDetailByEmailView.as_view(), name='user-detail-by-email'),
    
    # Endpoint to retrieve a specific user based on their ID.
    #path('User/get-id/<str:ids>/', UserDetailByIdView.as_view(), name='user-detail-by-id'),
]