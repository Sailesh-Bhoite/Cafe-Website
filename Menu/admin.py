from django.contrib import admin
from .models import MenuItem


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'image']


admin.site.register(MenuItem, MenuAdmin)
