from django.db import models


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=35)
    total_price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Vending_Location(models.Model):
    location_name = models.CharField(max_length=35)
    snack_prices = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.location_name