from django.db import models
from Menu.models import MenuItem
from Customers.models import Customer


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
