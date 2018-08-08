from django.db import models
from django.urls import reverse
from portfolio.fields import ThumbnailImageField
from accounts.models import User
from django.utils.text import slugify
from portfolio.models import PortfolioGroup

# Create your models here.
class ContentsType(models.Model):
	name = models.CharField(max_length=50, null=True)
	description = models.CharField('설명', max_length=100, blank=True)

	class Meta:
		verbose_name_plural = '쉼표-타입'
		ordering = ['-name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('contents:detail', args=(self.id,))


class Contents(models.Model):
	group = models.ForeignKey(PortfolioGroup, verbose_name="년도", on_delete=models.CASCADE)
	contents_type = models.ForeignKey(ContentsType, verbose_name="타입", blank=True, null=True, on_delete=models.CASCADE)

	title = models.CharField('제목', max_length=50)
	slug = models.SlugField('SLUG', unique=True, allow_unicode=True, null=True, help_text='자동 입력')
	image = ThumbnailImageField(verbose_name="대표 이미지", upload_to='portfolio/%Y/%m', blank=True, null=True)
	description = models.TextField('DESCRIPTION', blank=True)
	link = models.URLField('link', blank=True)
	upload_date = models.DateTimeField('작성일', auto_now_add=True)
	user = models.ForeignKey(User, verbose_name="작성자", null=True, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = '쉼표'
		ordering = ['-upload_date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('contents:detail', args=(self.slug,))


	def save(self, *args, **kargs):
		if not self.id:
			self.slug = slugify(self.title, allow_unicode=True)
		super(Contents, self).save(*args, **kargs)