from django.db import models

# This model is for handling queries, incidents and other questions from users.


class ContactForm(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    contact_method = models.CharField(
        max_length=10,
        choices=[('call', 'Call'), ('message', 'Send Message')]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "User Questions and Incidents"
