from django.db import models
from .models import *
from project.models import Project

class Process_Checklist(models.Model):
	GROUP_CHOICES = (
		('Code Quality', 'Code Quality'),
		('Processes', 'Processes'),
		('Quality Assurance', 'Quality Assurance'),
	)
	checklist_title = models.CharField(max_length=30)
	description = models.TextField()
	weightage = models.IntegerField(default=0)
	group = models.CharField(max_length=30, choices=GROUP_CHOICES, default='General')

class Audits(models.Model):
	STATUS_CHOICES = (
	('Blue', 'Blue Less Than 59 %'),
	('Red', 'Red 60 %'),
	('Orange', 'Orange 75 %'),
	('Green', 'Green 90%'),
	)
	project = models.ForeignKey(Project,on_delete=models.CASCADE)
	audit_title = models.CharField(max_length=30)
	date = models.DateField()
	status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Blue',)
	average_rating = models.IntegerField(default=0)
	general_comment = models.TextField()

class Audit_Items(models.Model):
	checklist = models.ForeignKey(Process_Checklist,on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	rating = models.IntegerField(default=0)
	audit = models.ForeignKey(Audits,on_delete=models.CASCADE)
	date = models.DateField(auto_now=True)
# Create your models here.
