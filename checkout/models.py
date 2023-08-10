import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from festivals.models import Festival
from profiles.models import UserProfile


# Information I need from the user to send the tickets.
class UserData(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')  # noqa
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    user_id = models.CharField(max_length=10, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)  # noqa
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # noqa
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)  # noqa

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line ticketpython3 is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0  # noqa
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100  # noqa
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Order information.


class Ticketing(models.Model):
    order = models.ForeignKey(UserData, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')  # noqa
    festival = models.ForeignKey(Festival, null=False, blank=False, on_delete=models.CASCADE)  # noqa
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)  # noqa

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the line ticket total
        and update the order total.
        """
        self.lineitem_total = self.festival.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.festival} on order {self.order.order_number}'
