from django.contrib import admin
from .models import Ad, Location, AdsLocation


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    filter_horizontal = ('locations',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


@admin.register(AdsLocation)
class AdsLocationAdmin(admin.ModelAdmin):
    list_display = ['ad', 'location', 'max_visits', 'start_date', 'end_date']



