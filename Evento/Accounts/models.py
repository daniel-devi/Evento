from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_to(instance, filename):
    """
    Generate the upload path for profile pictures.
    This function is used as the 'upload_to' parameter in the ImageField.
    """
    return f'profile_pictures/{filename}'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to=upload_to,
        blank=True,
        null=True,
        default='defaultUserImage.jpeg'
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        Return a string representation of the UserProfile instance.
        """
        return f"{self.user.username} Profile"