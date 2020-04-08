from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

from django.core.validators import MinLengthValidator


# Create your models here.
class Profile(models.Model):  # associating User model with Profile model
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # if profile is deleted, do not delete the user

    def __str__(self):
        return f'{self.user.username} Profile'


class Payment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # cc_number = CardNumberField('card number')
    # cc_expiry = CardExpiryField('expiration date')
    # cc_code = SecurityCodeField('security code')
    cc_number = models.CharField(max_length=20, validators=[MinLengthValidator(15)])
    cc_expiry = models.DateField(help_text="Please use the following format: <em>MM/YY</em>.")
    cc_code = models.CharField(max_length=3, help_text="Please use the following format: <em>CVV or CVC</em>.",
                               validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.cc_number}'


class Address(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    address_1 = models.CharField(max_length=30)
    address_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=60, default="Miami")
    state = models.CharField(max_length=30, default="Florida")
    zip_code = models.CharField(max_length=5, default="33199")
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.address_1


class Wishlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    wishlist = models.CharField(max_length=100000)
