from django.db import models
from django.contrib.humanize.templatetags.humanize import intcomma

# Create your models here.
class Qna(models.Model):
	name = models.CharField('이름', max_length=50)
	email = models.EmailField()
	subject = models.CharField('제목', max_length=50)
	content = models.TextField('내용')
	create_date = models.DateTimeField('Create Date', auto_now_add=True, null=True)
	budget = models.IntegerField()

	class Meta:
		verbose_name_plural = '문의'
		ordering = ['-create_date']

	def __str__(self):
		return self.subject

	def my_property(self):
		return intcomma(self.budget, False)+'원'

	number_format_budget = property(my_property)
	my_property.short_description = '예산'