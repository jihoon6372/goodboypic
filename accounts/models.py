from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):	
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        """
        전달된 이메일과 생년월일, 비밀번호로 유저를 생성하고 저장합니다.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        """
        전달된 이메일, 비밀번호로 슈퍼유저를 생성하고 저장합니다.
        """
        user = self.create_user(email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='이메일',
        max_length=190,
        unique=True,
        help_text='이메일주소를 입력해주세요.',
    )

    username = models.CharField(max_length=255, verbose_name='이름', blank=True)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='생년월일')
    is_active = models.BooleanField(default=True, verbose_name='활성', help_text='이 사용자가 활성화되어 있는지를 나타냅니다. 계정을 삭제하는 대신 이것을 선택 해제하세요.')
    is_admin = models.BooleanField(default=False, verbose_name='관리자', help_text='해당 사용자에게 모든 권한을 허가합니다.')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    class Meta:
        verbose_name_plural = '사용자 계정'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        # 유저는 이메일 주소로 식별됩니다.
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        "유저가 특정 허가를 받았습니까?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        "유저가 app을 볼 허가를 받았습니까?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        "유저가 staff입니까?"
        # Simplest possible answer: All admins are staff
        return self.is_admin