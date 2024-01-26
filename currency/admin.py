from django.contrib import admin

from .models import CurrencyRate


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('created', 'course', 'last_update')
    readonly_fields = ('created',)
    search_fields = ('created', 'last_update')
    ordering = ('-created',)
    list_per_page = 10
    list_filter = ('created', 'last_update')
