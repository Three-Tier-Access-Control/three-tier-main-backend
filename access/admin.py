from django.contrib import admin

from access.models import AccessLog

# Register your models here.
@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ("employee", "direction", "created")
    list_filter = ("employee", "direction",)
    date_hierarchy = 'created'
