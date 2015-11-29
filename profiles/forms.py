# forms.py
from django import forms
from django.contrib.auth import get_user_model

from .models import Profile

# FIXME: User와 1:1 관계인 Profile 클래스 내용을 Copy&Paste 하였다(gender)
# CopyPaste말고 UserForm에 포함할 수 있는 방법은 없을까?

class UserForm(forms.ModelForm):
    gender = forms.ChoiceField(required=True, widget=forms.Select, choices=Profile.GENDER_CHOICES)
    password = forms.CharField(widget=forms.PasswordInput, max_length=64)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'gender')
