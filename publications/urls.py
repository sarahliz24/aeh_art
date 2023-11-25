from django.urls import path
from . import views

urlpatterns = [
    path('', views.publications, name='publications'),
    path('<int:page>/', views.publications, name='publications_pages'),
]
