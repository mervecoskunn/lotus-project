from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Cart


@receiver(post_save, sender=Cart)
def create_empty_items(sender, instance, created, **kwargs):
    if created:
        instance.items.set([])
