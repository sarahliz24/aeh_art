from django.urls import path
from . import views

urlpatterns = [
    path('', views.awards, name='awards'),
    path('<int:page>/', views.awards, name='awards_pages'),
]
