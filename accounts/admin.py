from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    """
    새로운 유저를 생성하기 위한 폼. repeated password를 더한 모든 required 필드를 포함합니다.
    """
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        # 두개의 비밀번호가 일치하는지 확인합니다.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        # 비밀번호를 해시 형태로 저장합니다.
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    """
    유저를 업데이트하기위한 폼. 유저의 모든 필드를 포함합니다. 하지만 비밀번호 필드는 admin의 비밀번호 해시 표시 필드로 대체합니다.
    """
    password = ReadOnlyPasswordHashField(label='비밀번호', help_text="비밀번호는 원문 그대로 저장되지 않으므로, 사용자의 비밀번호를 볼 수 있는 방법은 없습니다. <a href='../password'>[ 비밀번호 변경 ]</a>")

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')
        

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # 유저가 제공하는 것에 상관없이, 처음 값을 리턴합니다.
        # This is done here, rather than on the field, because the
        # 필드에서 처리되는 것이 아니라 여기서 처리됩니다.
        # field does not have access to the initial value
        # 왜냐하면 필드가 처음 값에 접근할 수 없기 때문입니다.
        return self.initial["password"]


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    # 유저 인스턴스들을 추가하고 변경할 폼
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # 필드들은 유저 모델을 표시하는데 사용됩니다.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    #  auth.User의 특정 필드를 참조하는 UserAdmin을 오버라이드합니다.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('개인정보', {'fields': ('username', 'date_of_birth',)}),
        ('권한', {'fields': ('is_admin','is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets은 기본 ModelAdmin 속성이 아닙니다. 
    # UserAdmin이 유저 생성시에 사용하려고 get_fieldsets를 오버라이드합니다.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
# 이제 새로운 UserAdmin을 등록합니다.
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# 그리고, 우리는 장고의 built-in 허가를 사용하고 있지 않으므로,
# unregister the Group model from admin.
# admin에서 Group model을 제거합니다.

admin.site.unregister(Group)