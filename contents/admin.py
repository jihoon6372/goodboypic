from django.contrib import admin
from .models import Contents, ContentsType

# Register your models here.
class ContentsInline(admin.StackedInline):
	model = Contents
	extra = 2

class ContentsTypeAdmin(admin.ModelAdmin):
	inlines = [ContentsInline]
	list_display = ('name', 'description')

class ContentsAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'group', 'contents_type', 'upload_date')
	list_filter = ('contents_type','group',)
	prepopulated_fields = {'slug': ('title',)}
	list_per_page = 10

admin.site.register(Contents, ContentsAdmin)
admin.site.register(ContentsType, ContentsTypeAdmin)