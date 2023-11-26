from django.urls import path
from . import views


urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('wishlist_add/<int:artwork_id>/', views.wishlist_add,
         name='wishlist_add',),
    path('wishlist_remove/<int:artwork_id>/', views.wishlist_remove,
         name='wishlist_remove',),
]
