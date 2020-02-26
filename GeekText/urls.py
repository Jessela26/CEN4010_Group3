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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views

urlpatterns = [
                  url(r'^admin/', admin.site.urls, name='admin'),
                  url(r'^home/', views.homepage, name='home'),
                  url(r'^wishlist/$', views.wishlist, name='wishlist'),
                  url(r'^browse/', include('Browse.urls'), name='browse'),
                  url(r'^cart/$', views.cart, name='cart'),
                  url(r'^checkout/$', views.checkout, name='checkout'),
                  url(r'^$', RedirectView.as_view(url='home', permanent=True), name='index'),
                  path('author/<str:book_author>/', include('Author.urls'), name='author'),
                  path('browse/details/<int:book_id>/', include('BookDetails.urls'), name='details'),
                  url(r'register/$', user_views.register, name='register'),
                  url(r'login/$',
                      auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True),
                      name='login'),
                  # class based view
                  url(r'logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
                  # class based view
                  url(r'profile/$', user_views.profile, name='profile'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
