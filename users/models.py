from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


# Create your models here.
class Profile(models.Model):#associating User model with Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)#if profile is deleted, do not delete the user
    def __str__(self):
        return f'{self.user.username} Profile'



class Payment(models.Model):
    cc_number = CardNumberField('card number')
    cc_expiry = CardExpiryField('expiration date')
    cc_code = SecurityCodeField('security code')

    def __str__(self):
        return f'{self.user.username} Payment'

class Address(models.Model):
    address_1 = models.CharField(max_length=30)
    address_2 = models.CharField(max_length=50, blank = True)
    city = models.CharField(max_length=60, default="Miami")
    state = models.CharField(max_length=30, default="Florida")
    zip_code = models.CharField(max_length=5, default="33199")
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.address_1

