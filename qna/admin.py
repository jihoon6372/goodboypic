from django.contrib import admin
from .models import Qna
from django.contrib.humanize.templatetags.humanize import intcomma

# Register your models here.
class QnaAdmin(admin.ModelAdmin):
	list_display = ('name', 'subject', 'number_format_budget')
	readonly_fields=('name', 'email', 'number_format_budget', 'subject', 'content')
	list_per_page = 10
	
	# budget = intcomma(budget, False)
	fieldsets = [
		(None, {'fields': ['name', 'email', 'number_format_budget', 'subject', 'content']}),
	]


	def change_view(self, request, object_id, extra_context=None):
		# if not request.user.is_superuser:
		extra_context = extra_context or {}
		extra_context['show_save_and_continue'] = False
		extra_context['show_save'] = False

		return super(QnaAdmin, self).change_view(request, object_id, extra_context=extra_context)

	def has_add_permission(self, request):
		return False

	def has_change_permission(self, request, obj=None):
		return (request.method in ['GET', 'HEAD'] and super().has_change_permission(request, obj))

	def has_delete_permission(self, request, obj=None):
		return False

		

admin.site.register(Qna, QnaAdmin)
# admin.site.disable_action('delete_selected')