from django.contrib import admin
from .models import Customer, Product, ProductServices, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(ProductServices)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
