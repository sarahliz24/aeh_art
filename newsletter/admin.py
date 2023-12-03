from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    ''' Register newsletter in admin '''
    list_display = (
        'title',
        'date',
        'content',
    )


admin.site.register(Newsletter, NewsletterAdmin)
