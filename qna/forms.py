from django import forms
from .models import Qna

class QnaForm(forms.ModelForm):  

	class Meta:
		model = Qna
		fields = ('subject', 'name', 'email', 'budget', 'content')