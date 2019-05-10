# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('first_name', 'last_name','username', 'email', 'phone', 'designation', 'technology', 'year_of_exp')

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('username', 'email')


class RegisterUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span11'}))
	password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'span11'}))

	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name','username', 'email', 'phone', 'designation', 'technology', 'year_of_exp']
		widgets = {
		'first_name': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'last_name': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'username': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'email': forms.EmailInput(attrs={'class': 'span11', 'required': True}),
		'phone': forms.TextInput(attrs={'id': 'mask-phoneInt', 'class': 'span8 mask text','required': True}),
		'technology': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'designation': forms.Select(attrs={'required': True}),
		'year_of_exp': forms.NumberInput(attrs={'class': 'span11', 'required': True})
		}

    # Validating password
	def clean_password2(self):
		cd = self.cleaned_data
		
		if cd['password2'] != cd['password']:
			raise ValidationError("Password don't match")

		return cd['password2']

	def save(self, commit=True):
	# Save the provided password in hashed format
		user = super(RegisterUserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user


class UserUpdateForm(forms.ModelForm):
	
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name','username', 'email', 'phone', 'designation', 'technology', 'year_of_exp']
		widgets = {
		'first_name': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'last_name': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'username': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'email': forms.EmailInput(attrs={'class': 'span11', 'required': True}),
		'phone': forms.TextInput(attrs={'id': 'mask-phoneInt', 'class': 'span11 mask text','required': True}),
		'technology': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'designation': forms.Select(attrs={'required': True}),
		'year_of_exp': forms.NumberInput(attrs={'class': 'span11', 'required': True})
		}


'''class UserReg(forms.Form):
	first_name = models.CharField(max_length=30, blank=True, attrs={'class': 'span11'})
	last_name = models.CharField(max_length=30, blank=True, attrs={'class': 'span11'})
	username = models.CharField(max_length=30, blank=True, attrs={'class': 'span11'})
	email = models.CharField(max_length=30, blank=True, attrs={'class': 'span11'})
	phone = models.IntegerField(null=True)
	year_of_exp = models.IntegerField(default=0)
	designation = models.CharField(max_length=30, blank=True, attrs={'class': 'span11'})
	technology = models.CharField(max_length=30, blank=True, attrs={'class': 'span11'})
	password = models.CharField(max_length=30, blank=True)'''