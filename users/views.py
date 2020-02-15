from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required #url restrictions
from .forms import UserRegisterForm

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
    return render(request, 'users/profile.html')
