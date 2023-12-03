from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    ''' Register Product in admin '''
    list_display = (
        'artwork_id',
        'title',
        'description',
        'price',
        'year',
        'image',
    )

    ordering = ('artwork_id',)


class CategoryAdmin(admin.ModelAdmin):
    ''' Register category in admin '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
