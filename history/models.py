from django.db import models
from portfolio.models import PortfolioGroup

# Create your models here.
class History(models.Model):
	title = models.CharField(max_length=255, null=True)
	group = models.ForeignKey(PortfolioGroup, verbose_name="년도", null=True, on_delete=models.CASCADE)
	create_date = models.DateTimeField('Create Date', auto_now_add=True, null=True)

	class Meta:
		verbose_name_plural = '연혁'
	
	def __str__(self):
		return self.title