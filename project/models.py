from django.db import models
from user.models import CustomUser

class Project(models.Model):
	title = models.CharField(max_length=50)
	abstract = models.TextField()
	team_size = models.IntegerField(default=0)
	technology_stack = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	git_hub_link = models.URLField()
	team_lead = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
	def __str__(self):
		return self.title
# Create your models here.
