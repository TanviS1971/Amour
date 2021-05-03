from django.contrib import admin
from .models import Item, Order, OrderItem, Address

class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'price', 'discount_price']


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'street_address',
        'apartment_address',
        'city',
        'pin',
        'default'
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)