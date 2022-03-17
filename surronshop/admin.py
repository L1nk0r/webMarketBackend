from django.contrib import admin
from .models import Product, Image, Cart, CartProduct, Customer, Specifications, Order, HandMadeOrder

# Register your models here.
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Specifications)
admin.site.register(Order)
admin.site.register(HandMadeOrder)
