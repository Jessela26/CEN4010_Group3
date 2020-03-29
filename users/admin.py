from django.contrib import admin
from .models import Profile, Payment, Address

# Register your models here.
admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(Address)