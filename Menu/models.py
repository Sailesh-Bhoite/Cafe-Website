from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=255)
    image = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.name
