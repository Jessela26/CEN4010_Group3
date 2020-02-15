"""GeekText URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.homepage, name = 'geektext-home'),
    url(r'^wishlist/$', views.wishlist),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), #class based view
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'), #class based view
    path('profile/', user_views.profile, name = 'profile'),
]
