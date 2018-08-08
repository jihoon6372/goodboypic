from django.contrib import admin
from .models import BlockIP, DevModeAllowIP

# Register your models here.
class BlockIPAdmin(admin.ModelAdmin):
	list_display = ('id', 'ip_address', 'memo',)


class DevModeAllowIPAdmin(admin.ModelAdmin):
	list_display = ('id', 'ip_address', 'memo',)


admin.site.register(BlockIP, BlockIPAdmin)
admin.site.register(DevModeAllowIP, DevModeAllowIPAdmin)
