from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Project
from user.models import CustomUser
from django.core.exceptions import ValidationError

class RegisterUserForm(forms.ModelForm):
	team_lead = forms.ModelChoiceField(queryset=CustomUser.objects.filter(designation="Tech Lead"),empty_label="Select Tech Lead for Project")
	abstract=forms.CharField( widget=forms.Textarea )
	technology_stack=forms.CharField( widget=forms.Textarea )

	class Meta:
		model = Project
		fields = ['title', 'abstract', 'team_lead','team_size', 'technology_stack', 'start_date', 'end_date', 'git_hub_link']
		widgets = {
		'title': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		#'abstract': forms.TextArea(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'team_size': forms.NumberInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		#'technology_stack': forms.TextArea(attrs={'class': 'span11', 'required': True}),
		'start_date': forms.DateInput(attrs={'class': 'datepicker span11','required': True}),
		'end_date': forms.DateInput(attrs={'class': 'datepicker span11', 'autofocus': True, 'required': True}),
		'git_hub_link': forms.URLInput(attrs={'required': True}),
		}