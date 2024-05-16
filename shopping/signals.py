from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Cart


@receiver(post_save, sender=Cart)
def create_empty_items(sender, instance, created, **kwargs):
    """
    Signal handler to create an empty items list when a Cart is created.
    """
    if created:
        instance.items.set([])
