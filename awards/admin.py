from django.contrib import admin
from .models import Awards


class AwardsAdmin(admin.ModelAdmin):
    ''' Register awards in admin '''
    list_display = (
        'award_title',
        'award_year',
        'award_info',
    )


admin.site.register(Awards, AwardsAdmin)
