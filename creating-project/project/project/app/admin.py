from django.contrib import admin
from app.models import Station, Route


class StationAdmin(admin.ModelAdmin):
    pass


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
