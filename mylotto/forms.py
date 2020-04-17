from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):
	class Meta:
		model = GuessNumbers
		fields =('name','text','num_lotto',)
		#입력 받을 것 따로 설정