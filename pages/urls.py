from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('artist/', views.artist, name='artist'),
    path('scientist/', views.scientist, name='scientist'),
    path('human/', views.human, name='human'),
    path('shop_info/', views.shop_info, name='shop_info'),
]
