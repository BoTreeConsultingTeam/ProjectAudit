from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	DESIGNATION_CHOICES = (
	('Tech Lead', 'Tech Lead'),
	('Q/A', 'Q/A'),
	('Developer', 'Developer'),
	('UI Designer', 'UI Designer'),
	)
	year_of_exp = models.IntegerField(default=0)
	designation = models.CharField(max_length=30, choices=DESIGNATION_CHOICES, default='Tech Lead',)
	technology = models.CharField(max_length=30, blank=True)
	phone = models.CharField(max_length=30, null=True)

	def __str__(self):
		return self.username


# Create your models here.
