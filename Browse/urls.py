from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.browse, name='home'),
    path('by_title', views.browse, name='browse'),
    path('by_title&view_18', views.browse18, name='browse18'),
    path('sort/by_author', views.author, name='by_author'),
    path('sort/by_author&view_18', views.author18, name='by_author18'),
    path('sort/recent', views.p_date_new2old, name='p_date_new2old'),
    path('sort/recent&view_18', views.p_date_new2old18, name='p_date_new2old18'),
    path('sort/older', views.p_date_old2new, name='p_date_old2new'),
    path('sort/older&view_18', views.p_date_old2new18, name='p_date_old2new18'),
    path('search/', views.browse, name='search')
]
