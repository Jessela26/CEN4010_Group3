from django.contrib import admin
from .models import Profile, Payment, Address, Wishlist, ShoppingCart

# Register your models here.
admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(Address)
admin.site.register(Wishlist)
admin.site.register(ShoppingCart)