from django.contrib import admin
from svinfo.models import Service, Role, Status, OS, LB, Server

class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['service_id', 'service_name']}),
    ]
    list_display = ('service_id', 'service_name')

class RoleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['role_name']}),
    ]

class StatusAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['status_name']}),
    ]

class OSAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['os_name']}),
    ]

class LBAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['lb_name']}),
    ]

class ServerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {'fields': ['hostname', 'service', 'role', 'status', 'os', 'ip4', 'ip6', 'lb', 'comment']}),
        ('OpenNMS', {'fields': ['opennms_id', 'opennms_host', 'opennms_mac'], 'classes': ['collapse']}),
    ]
    list_display = ('hostname', 'service', 'role', 'status', 'os', 'ip4', 'lb', 'comment')
    list_filter = ['service', 'status', 'os']
    search_fields = ['hostname']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(OS, OSAdmin)
admin.site.register(LB, LBAdmin)
admin.site.register(Server, ServerAdmin)
