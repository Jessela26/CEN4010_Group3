from django import forms
from django.contrib.auth.models import User
from users.models import Payment, Address
from django.contrib.auth.forms import UserCreationForm
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    


    class Meta: #namespace for configurations for user models
        model = User
        fields = ['username', 'email','first_name', 'last_name','password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']



class PaymentForm(forms.ModelForm):
    cc_number = CardNumberField(label='Card Number')
    cc_expiry = CardExpiryField(label='Expiration Date')
    cc_code = SecurityCodeField(label='CVV/CVC')

    class Meta:
        model = Payment
        fields = ['cc_number', 'cc_expiry','cc_code']

class AddressForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=30)
    address_2 = forms.CharField(max_length=50, required = False)
    city = forms.CharField(max_length=60)
    state = forms.CharField(max_length=30)
    zip_code = forms.CharField(max_length=5)
    country = forms.CharField(max_length=50)

    class Meta:
        model = Address
        fields = ['address_1','address_2','city','state','zip_code', 'country']


