from django import forms
from .models import UserInfos

class SignUpForm(forms.ModelForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

	class Meta:
		model = UserInfos
		fields = ("username",)

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if UserInfos.objects.filter(username=username).exists():
			raise forms.ValidationError("This username already exists")
		return username

	def clean(self):
		cleaned_data = super().clean()
		pwd1 = cleaned_data.get("password1")
		pwd2 = cleaned_data.get("password2")
		if pwd1 and pwd2 and pwd1 != pwd2:
			raise forms.ValidationError("Passwords do not match")
		return cleaned_data

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
	
class SignInForm(forms.Form):
	username = forms.CharField(max_length=32)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get("username")
		password = cleaned_data.get("password")

		if not password:
			self.add_error("username", "Username needed")
		if not username:
			self.add_error("password", "Password needed")

		return cleaned_data
				