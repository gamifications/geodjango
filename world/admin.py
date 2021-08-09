from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin, GeoModelAdmin
from .models import Shop, WorldBorder

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')



admin.site.register(WorldBorder, GeoModelAdmin)