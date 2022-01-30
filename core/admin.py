from django.contrib import admin
from .models import LocationEntryJson, LocationEntry, TransitionEntry, WayPointsEntry, WaypointEntry
# Register your models here.
class LocationEntryJsonAdmin(admin.ModelAdmin):
    list_display = ('id','dtst', 'data',)
admin.site.register(LocationEntryJson, LocationEntryJsonAdmin)


class LocationentryAdmin(admin.ModelAdmin):
    list_display = ('id','dtst', 'inregions_display', '_type', 'BSSID', 'SSID', 'acc', 'alt', 'batt', 'bs', 'conn', 'created_at', 'lat', 'lon', 't', 'tid', 'topic', 'tst', 'vac', 'vel')    
admin.site.register(LocationEntry, LocationentryAdmin)

class WaypointentryAdmin(admin.ModelAdmin):
    list_display = ('id','dtst', '_type', 'desc', 'lat', 'lon', 'rad', 'topic', 'tst')
admin.site.register(WaypointEntry, WaypointentryAdmin)
class WaypointsentryAdmin(admin.ModelAdmin):
    list_display = ('id', '_type', 'topic',)
    filter_horizontal = ('waypoints',)
admin.site.register(WayPointsEntry, WaypointsentryAdmin)
class TransitionEntryAdmin(admin.ModelAdmin):
    list_display = ('id','dtst', '_type', 'acc', 'desc', 'event', 'lat', 'lon', 't', 'tid', 'topic', 'tst', 'wtst')
admin.site.register(TransitionEntry, TransitionEntryAdmin)