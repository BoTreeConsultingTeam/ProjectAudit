from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Process_Checklist, Audits, Audit_Items
from django.core.exceptions import ValidationError
from project.models import Project

class Process_Checklist_Entry(forms.ModelForm):
	description=forms.CharField( widget=forms.Textarea )
	#group = forms.ModelChoiceField(queryset=Project.objects.all())

	class Meta:
		model = Process_Checklist
		fields = ['group','checklist_title', 'description', 'weightage']
		widgets = {
		'checklist_title': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'weightage': forms.NumberInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'group': forms.Select(attrs={'required': True}),
		}

class AuditForm(forms.ModelForm):
	project=forms.ModelChoiceField(queryset=Project.objects.all())
	general_comment=forms.CharField( widget=forms.Textarea )

	'''def __init__(self, args, *kwargs):
		super().__init__(*args, **kwargs)
		self.fields['city'].queryset = City.objects.none()
		if 'state' in self.data:
			self.fields['city'].queryset = City.objects.filter(state_id=self.data['state'])'''

	class Meta:
		model=Audits
		fields = ['project', 'audit_title', 'general_comment', 'status','date']
		widgets = {
		'checklist_title': forms.TextInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'weightage': forms.NumberInput(attrs={'class': 'span11', 'autofocus': True, 'required': True}),
		'status': forms.Select(attrs={'required': True}),
		'date': forms.DateInput(attrs={'class': 'datepicker span11','required': True}),
		}

class ChecklistForm(forms.ModelForm):

	class Meta:
		model=Audit_Items
		fields = ['comment','rating']