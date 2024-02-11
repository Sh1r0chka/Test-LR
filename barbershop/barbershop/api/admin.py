from django.contrib import admin
from .models import Services, Orders


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title', 'price')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_order', 'services', 'description', 'owner')
    list_display_links = ('id', 'date_of_order', 'services', 'description', 'owner')
