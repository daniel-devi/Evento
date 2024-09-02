from django.contrib import admin
from .models import UserProfile

# Register your models here.

# Register the UserProfile model with the custom admin class
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin list view
    list_display = ('user', 'phone_number', 'address', 'city', 'country')
    
    # Define the fields that can be searched in the admin interface
    search_fields = ('user__username', 'first_name', 'last_name', 'email', 'phone_number')
    

