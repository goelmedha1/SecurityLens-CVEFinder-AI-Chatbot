from django.contrib import admin
from .models import SearchQuery

# Register your models here.

@admin.register(SearchQuery)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('id','query', 'result', 'timestamp')

# admin.site.register(SearchQuery, SearchAdmin)