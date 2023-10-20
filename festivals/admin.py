from django.contrib import admin
from .models import Festival

# Register your models here.


class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'price')
    list_filter = ('date', 'location')
    search_fields = ('name', 'location')


admin.site.register(Festival, FestivalAdmin)
