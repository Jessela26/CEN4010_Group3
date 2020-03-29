from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required #url restrictions
from .forms import UserRegisterForm, UpdateUserForm, PaymentForm, AddressForm

def register(request):
    if request.method == 'POST':#data in form
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#get python formatted data from request
            messages.success(request, f'Account Created! You can log in now.')
            return redirect('login')
    else:
        form = UserRegisterForm()#empty form
    return render(request, 'users/register.html', {'form': form})

@login_required#user must be logged in to view this page
def profile(request):
    if request.method == 'POST':#data in form
        u_form = UpdateUserForm(request.POST, instance = request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('profile')
    else:
        u_form = UpdateUserForm( instance = request.user)
    context = {
        'u_form': u_form,
    } 
    return render(request, 'users/profile.html', context)



@login_required#user must be logged in to view this page
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your password was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request,('Please correct the error(s) below.'))
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'users/change_password.html', context)

@login_required
def payment_info(request):
    if request.method == 'POST':
        p_form = PaymentForm(request.POST)
        if p_form.is_valid():
            user = p_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Payment Information Updated!'))
            return redirect('profile')
        else:
            messages.error(request,('Please correct the error(s) below.'))
    else:
        p_form = PaymentForm(request.POST)
    context = {
        'p_form': p_form
    }
    return render(request, 'users/payment.html', context)

@login_required
def shipping_info(request):
    if request.method == 'POST':
        s_form = AddressForm(request.POST)
        if s_form.is_valid():
            user = s_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Shipping Information Updated!'))
            return redirect('profile')
        else:
            messages.error(request,('Please correct the error(s) below.'))
    else:
        s_form = AddressForm(request.POST)
    context = {
        's_form': s_form
    }
    return render(request, 'users/shipping.html', context)

