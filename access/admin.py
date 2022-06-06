from django.contrib import admin

from access.models import AccessLog

# Register your models here.
@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ("employee", "direction", "status" "created")
    list_filter = ("employee", "direction", "status")
    date_hierarchy = 'created'
