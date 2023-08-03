from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Ticketing


@receiver(post_save, sender=Ticketing)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on line ticket update/create.
    """
    instance.order.update_total()


@receiver(post_delete, sender=Ticketing)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on line ticket delete.
    """
    instance.order.update_total()
