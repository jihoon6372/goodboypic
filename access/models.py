from django.db import models

# Create your models here.
class BlockIP(models.Model):
	class Meta:
		verbose_name_plural = '접속 차단 IP'
			
	ip_address = models.CharField(max_length=512, help_text='접속 차단 할 IP를 등록하세요.')
	memo = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.ip_address


class DevModeAllowIP(models.Model):
	class Meta:
		verbose_name_plural = '개발모드 접속 허용 IP'

	ip_address = models.CharField(max_length=512, help_text='개발자 모드에서 접속 허용할 IP를 등록하세요.')
	memo = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.ip_address