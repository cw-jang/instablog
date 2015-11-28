# forms.py

from django import forms

from .models import Post


class PostForm(forms.ModelForm):
	# title = forms.CharField(widget=forms.PasswordInput)
	# 이 경우는 여기 선언된 title로 오버라이드 된다 

	def clean(self):
		title = self.cleaned_data.get('title', '')
		if '지각' in title:
			self.add_error('title', '지각자!!!')
		return None

	# def clean_title(self):
	# 	title = self.cleaned_data.get('title', '')
	# 	if '지각' in title:
	# 		raise forms.ValidationError(
	# 				'지각자 이름이 있습니다!', 
	# 				code='strange_word')
	#	return title

	class Meta:
		model = Post
		# fields = '__all__'
		fields = ('category', 'title', 'content', )
		# widgets = {
		# 	'title': forms.PasswordInput
		# }


class PostNormalForm(forms.Form):
	title = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()
	category = forms.IntegerField(0)
	# registration_code = forms.CharField(
	# 	label = '주민번호', 
	# 	help_text = 'xxxxyyyy', 
	# 	widget = forms.TextInput(
	# 		attrs={'class': 'hello_world'}
	# 	)
