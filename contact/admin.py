from django.contrib import admin
from .models import UserContactForm


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'submitted_at', 
    )

admin.site.register(UserContactForm)
