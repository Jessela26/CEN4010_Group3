from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.browse, name='browse'),
    path('sort/by_author/', views.author, name='by_author'),
    path('sort/recent/', views.p_date_new2old, name='p_date_new2old'),
    path('sort/older/', views.p_date_old2new, name='p_date_old2new'),
    url('search/$', views.browse, name='search')
]
