# shortenURL/admin.py

from django.contrib import admin
from shortenURL.models import Shorten


@admin.register(Shorten)
class ShortenAdmin(admin.ModelAdmin):
    
    list_display = ('url', 'code', 'date', 'nb_acces')
    list_filter = ('date',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('url', 'date')
