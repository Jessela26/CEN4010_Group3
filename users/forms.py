from django import forms
from django.contrib.auth.models import User
from users.models import Payment
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


