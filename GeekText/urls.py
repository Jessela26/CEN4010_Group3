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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^home/', views.homepage, name='home'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),
    url(r'^browse/', include('Browse.urls'), name='browse'),
    url(r'cart/$', views.cart, name='cart'),
    url(r'^$', RedirectView.as_view(url='home', permanent=True), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
