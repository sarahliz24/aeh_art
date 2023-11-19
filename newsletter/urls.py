from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('<int:newsletter_id>/', views.newsletter_detail, name='newsletter_detail'),
    path('add/', views.add_newsletter, name='add_newsletter'),
    path('edit/<int:newsletter_id>/', views.edit_newsletter, name='edit_newsletter'),
    path('delete/<int:newsletter_id>/', views.delete_newsletter,name='delete_newsletter'),
]
