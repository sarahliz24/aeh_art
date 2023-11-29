from django.contrib import admin
from .models import Publications


class PublicationsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'authors',
        'publication_year',
        'source',
        'volume_number',
        'page_range',
        'doi',
    )


admin.site.register(Publications, PublicationsAdmin)
