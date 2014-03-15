from django.contrib import admin
from svinfo.models import Service, Os, Status, Server

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['service_id', 'service_name']}),
    ]
    list_display = ('service_id', 'service_name')

class OsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['os_name']}),
    ]

class StatusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['status_name']}),
    ]

class ServerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['hostname', 'status', 'os', 'service']}),
    ]
    list_display = ('hostname', 'status', 'os', 'service')
    list_filter = ['status', 'os', 'service']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Os, OsAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Server, ServerAdmin)
