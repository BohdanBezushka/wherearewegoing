from django.db import models

# Create your models here:

# Register a festival to sell tickets


class Festival(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    festival_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
