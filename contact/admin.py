from django.contrib import admin
from .models import UserContactForm


class ContactAdmin(admin.ModelAdmin):
    ''' Register contact in admin '''
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'submitted_at',
    )


admin.site.register(UserContactForm, ContactAdmin)
