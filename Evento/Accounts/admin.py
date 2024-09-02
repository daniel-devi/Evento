from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the admin list view
    list_display = ('user', 'phone_number', 'address', 'city', 'country')
    
    # Add a filter option for the country field in the admin interface
    list_filter = ('country',)
    
    # Define the fields that can be searched in the admin interface
    search_fields = ('user__username', 'first_name', 'last_name', 'email', 'phone_number')
    
    # Make the 'user' field read-only to prevent modifications
    readonly_fields = ('user',)


# Register the UserProfile model with the custom admin class
admin.site.register(UserProfile, UserProfileAdmin)