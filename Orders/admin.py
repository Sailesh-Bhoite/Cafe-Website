from django.contrib import admin
from Orders.models import Order, OrderItem


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_date', 'total_price', 'customer']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'menu_item', 'quantity', 'price']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
