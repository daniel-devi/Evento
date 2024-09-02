from django.contrib.auth.models import User
from Accounts.models import UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function that creates a UserProfile instance
    whenever a new User instance is created.

    Args:
        sender: The model class sending the signal (User in this case)
        instance: The actual instance of the User model being saved
        created: Boolean flag indicating if this is a new User instance
        **kwargs: Additional keyword arguments
    """
    if created:
        UserProfile.objects.create(user=instance)
