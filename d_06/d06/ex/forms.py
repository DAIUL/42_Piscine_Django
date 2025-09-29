from django import forms
from .models import UserInfos, Tip
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
	class Meta:
		model = UserInfos
		fields = ("username", "password1", "password2")
	
class SignInForm(AuthenticationForm):
	class Meta:
		model = UserInfos
		fields = ("username", "password")

class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ["content"]
				