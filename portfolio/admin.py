from django.contrib import admin
from portfolio.models import Portfolio, PortfolioGroup

# Register your models here.
class PortfolioInline(admin.StackedInline):
	model = Portfolio
	extra = 2
	prepopulated_fields = {'slug': ('title',)}

class PortfolioGroupAdmin(admin.ModelAdmin):
	inlines = [PortfolioInline]
	list_display = ('name', 'description')
	list_per_page = 10

class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'group', 'upload_date')
	list_filter = ('group',)
	prepopulated_fields = {'slug': ('title',)}
	list_per_page = 10

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioGroup, PortfolioGroupAdmin)