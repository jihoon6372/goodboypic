from django.contrib import admin
from .models import AuthLog

# Register your models here.
class AuthLogAdmin(admin.ModelAdmin):
	list_display = ('user', 'ip_address', 'user_agent', 'auth_date')
	readonly_fields=('user', 'ip_address', 'user_agent', 'auth_date')
	list_per_page = 10
	list_filter = ('user',)

	def change_view(self, request, object_id, extra_context=None):
		extra_context = extra_context or {}
		extra_context['show_save_and_continue'] = False
		extra_context['show_save'] = False

		return super(AuthLogAdmin, self).change_view(request, object_id, extra_context=extra_context)

	def has_add_permission(self, request):
		return False

	def has_change_permission(self, request, obj=None):
		return (request.method in ['GET', 'HEAD'] and super().has_change_permission(request, obj))

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(AuthLog, AuthLogAdmin)