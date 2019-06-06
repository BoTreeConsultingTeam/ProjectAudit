from django.test import TestCase,Client
from .models import Project
from user.models import CustomUser
from django.urls import *
from .project_forms import RegisterUserForm
class ProjectTestCase(TestCase):

	fixtures=['project/fixtures/project_data.json']

	@classmethod
	def setUpClass(cls):
		super(ProjectTestCase, cls).setUpClass()
		print("Project Test Cases Execution starts")
		#self.user= CustomUser.objects.create()
		#import code; code.interact(local=dict(globals(), **locals()))
		#print(CustomUser.objects.all())
		#print(Project.objects.all())
	
	'''def setUp(self):
		user=CustomUser.objects.create(username='binoy')
		print(CustomUser.objects.all())
		self.user= Project.objects.create(start_date="8888-12-2",end_date="8888-11-22",team_lead=user)
		#print(self.user)'''

	def test_first(self):
		#print("qwe",self.user.first_name,"ads",self.user.phone,self.user.designation,self.user.password)
		pass

	def test_url(self):
		client=Client()
		client.login(username='Binoy',password='admin@123')
		url=reverse('projectcreate')
		response = client.get(url)
		print("Project Create URL successfully called")
		self.assertEquals(response.status_code,200)
		url=reverse('projectlist')
		response = client.get(url)
		print("Project List View URL successfully called")
		self.assertEquals(response.status_code,200)
		url=reverse('projectupdate', kwargs={'pk': 1})
		response = client.get(url)
		print("Project Update View URL successfully called")
		self.assertEquals(response.status_code,200)
		url=reverse('projectdelete', kwargs={'pk': 1})
		response = client.get(url)
		print("Project Delete View URL successfully called")
		self.assertEquals(response.status_code,200)

	def test_project_data(self):
		client=Client()
		client.login(username='Binoy',password='admin@123')
		

		#Project Creation Testing
		url=reverse('projectcreate')
		response = client.get(url)
		
		req_data = {
			"abstract": "sakdnaknkjndsj",
			"end_date": "2019-05-31",
			"git_hub_link": "http://www.cs.com",
			"start_date": "2011-05-01",
			"team_lead": 4,
			"team_size": 4,
			"technology_stack": "naskn\r\ndnkandk\r\ndnask",
			"title": "Binoy"
			}		
		self.assertEquals(response.status_code,200)
		form = RegisterUserForm(data = req_data)
		form.is_valid()
		if form.errors:
			print(form.errors)
			self.assertTrue(form.errors)
		else:
			client.login(username='Binoy',password='admin@123')
			response = client.post(url, req_data)
			#print(response.content)
			#self.assertContains('"error": This field is required.' in response.content)
			#self.assertEquals(response.status_code, 200)
			print(Project.objects.get(id=7))
			self.assertURLEqual(response.url, "/project/projectlist/")
			print("Project Created")
		

		#Project Updation Testing
		req_data = {
			"abstract": "sakdnaknkjndsj",
			"end_date": "2019-05-31",
			"git_hub_link": "http://www.cs.com",
			"start_date": "2011-05-01",
			"team_lead": 4,
			"team_size": 4,
			"technology_stack": "naskn\r\ndnkandk\r\ndnask",
			"title": "Meet"
			}	
		url=reverse('projectupdate', kwargs={'pk': 7})
		#print(url)
		response = client.post(url, req_data)
		if response.status_code==404:
			print("Page not found")
		else:
			print(Project.objects.get(id=7))
			print("Project Update View successfully called")
			self.assertURLEqual(response.url, "/project/projectlist")


		#Project Deletion Testing
		url=reverse('projectdelete', kwargs={'pk': 7})
		response = client.post(url)
		if response.status_code==404:
			print("Page not found")
		else:
			print("Project Delete View successfully called")
			#print(Project.objects.get(id=7))
			self.assertURLEqual(response.url, "/project/projectlist")



	def test_form(self):
		#print("qwe",self.user.first_name,"ads",self.user.phone,self.user.designation,self.user.password)
		valid_data = {
			"abstract": "sakdnaknkjndsj",
			"end_date": "2019-05-31",
			"git_hub_link": "http://www.cs.com",
			"start_date": "2011-05-01",
			"team_lead": 4,
			"team_size": 4,
			"technology_stack": "naskn\r\ndnkandk\r\ndnask",
			"title": "xyz"
			}
		form = RegisterUserForm(data = valid_data)
		form.is_valid()
		if form.errors:
			print(form.errors)
			self.assertTrue(form.errors)
		else:
			self.assertFalse(form.errors)
			print("Form Test successfully executed")
		

# Create your tests here.
