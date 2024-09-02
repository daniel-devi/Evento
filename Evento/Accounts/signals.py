from Accounts.models import UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=UserProfile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
