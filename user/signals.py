from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Cart


@receiver(post_save, sender=Profile)
def create_empty_cart(sender, instance, created, **kwargs):
    """
    Signal handler to create an empty cart when a Profile is created.
    """
    if created:
        # Create an empty cart associated with the newly created Profile
        Cart.objects.create(profile=instance).save()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a Profile when a User is created.
    """
    if created:
        # Create a Profile associated with the newly created User
        Profile.objects.create(user=instance).save()
