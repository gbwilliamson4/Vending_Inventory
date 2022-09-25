from django.db import models
from datetime import datetime


# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=35)
    total_price = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Vending_Location(models.Model):
    location_name = models.CharField(max_length=35)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.location_name


class Vending_Inventory(models.Model):
    location = models.ForeignKey(Vending_Location, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.location) + " - " + str(self.item)


class Purchase_History(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Purchase History"

    def __str__(self):
        return str(self.item) + " - " + str(self.purchase_date)


class Needed_Inventory(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)
    admin_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Needed Inventory"

    def __str__(self):
        return str(self.item)
