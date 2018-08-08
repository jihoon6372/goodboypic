from django.contrib import admin
from history.models import History

# Register your models here.
class HistoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'group', 'create_date')
	list_filter = ('group',)
	list_per_page = 10

admin.site.register(History, HistoryAdmin)