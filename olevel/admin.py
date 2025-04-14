from django.contrib import admin
from .models import OLevelMark

@admin.register(OLevelMark)
class OLevelMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'score', 'term', 'year']
    list_filter = ['term', 'year', 'subject']
    search_fields = ['student__name']
