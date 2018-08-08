from django.db import models
from accounts.models import User

# Create your models here.
class AuthLog(models.Model):
	class Meta:
		verbose_name_plural = '로그인 기록'

	user = models.ForeignKey(User, null=True, verbose_name = '로그인 계정', on_delete=models.CASCADE)
	ip_address = models.CharField(max_length=512, null=True)
	user_agent = models.CharField(max_length=255, null=True)
	auth_date = models.DateTimeField('접속일', auto_now_add=True)