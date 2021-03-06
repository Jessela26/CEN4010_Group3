from django.urls import path

from . import views

urlpatterns = [
    path('', views.browse, name='home'),
    path('sort/by_title', views.browse, name='browse'),
    path('sort/by_title&view_18', views.browse18, name='browse18'),
    path('sort/by_author', views.author, name='by_author'),
    path('sort/by_author&view_18', views.author18, name='by_author18'),
    path('sort/recent', views.p_date_new2old, name='p_date_new2old'),
    path('sort/recent&view_18', views.p_date_new2old18, name='p_date_new2old18'),
    path('sort/older', views.p_date_old2new, name='p_date_old2new'),
    path('sort/older&view_18', views.p_date_old2new18, name='p_date_old2new18'),
    path('sort/price_lth', views.price_low_to_high, name='p_lth'),
    path('sort/price_lth18', views.price_low_to_high18, name='p_lth18'),
    path('sort/price_htl', views.price_high_to_low, name='p_htl'),
    path('sort/price_htl18', views.price_high_to_low18, name='p_htl18'),
    path('sort/by_genre/<str:book_genre>', views.by_genre, name='by_genre'),
    path('sort/title_desc', views.title_desc, name='title_desc'),
    path('sort/title_desc18', views.title_desc18, name='title_desc18'),
    path('sort/top_seller', views.top_sell, name='top_sell'),
    path('sort/rating_ascending', views.rating_asc, name='rating_asc'),
    path('sort/rating_ascending18', views.rating_asc18, name='rating_asc18'),
    path('sort/rating_descending', views.rating_desc, name='rating_desc'),
    path('sort/rating_descending18', views.rating_desc18, name='rating_desc18'),
    path('search/', views.browse, name='search')
]
