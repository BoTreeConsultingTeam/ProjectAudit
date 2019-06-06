from django.test import TestCase,Client
from .models import *
from user.models import CustomUser
from django.urls import *
from .audit_forms import *
class UserTestCase(TestCase):
	

	fixtures=['audit/fixtures/audit_data.json']

	@classmethod
	def setUpClass(cls):
		super(UserTestCase, cls).setUpClass()
		print("Audit Test Cases Execution starts")
		

	def test_aaurl(self):
		client=Client()
		client.login(username='Binoy',password='admin@123')

		url=reverse('checklistentry')
		response = client.get(url)
		print("Checklist Entry page URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('checklistview')
		response = client.get(url)
		print("Checklist View page URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('checklistupdate', kwargs={'pk': 3})
		response = client.get(url)
		print("Checklist Update View URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('checklistdelete', kwargs={'pk': 3})
		response = client.get(url)
		print("Checklist Delete View URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('auditreport')
		response = client.get(url)
		print("Audit Report Entry page URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('auditreportview')
		response = client.get(url)
		print("Audit Report View page URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('audititemsview')
		response = client.get(url,{'id':'1'})
		print(response)
		print("Audit Report Items View page URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('auditchart', kwargs={'pk': 1})
		response = client.get(url)
		print("Audit Chart View URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('auditupdate', kwargs={'pk': 1})
		response = client.get(url)
		print("Audit Update View URL successfully called")
		self.assertEquals(response.status_code,200)
		
		url=reverse('chart', kwargs={'pk': 1})
		response = client.get(url)
		print("Audit Chart View URL successfully called")
		self.assertEquals(response.status_code,200)

	def test_aInsert(self):
		client=Client()
		client.login(username='Binoy',password='admin@123')
		

		#Project Creation Testing
		url=reverse('checklistentry')
		response = client.get(url)
		
		req_data = {
			"checklist_title": "Code Review",
			"description": "Checks whether the code is optimized, standard and error free.",
			"weightage": 40,
			"group": "Code Quality"
		}		
		self.assertEquals(response.status_code,200)
		form = Process_Checklist_Entry(data = req_data)
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
			print(Process_Checklist.objects.get(id=Process_Checklist.objects.latest('id').id))
			self.rowdyid=Process_Checklist.objects.latest('id').id
			print("Create ma je id che e che:", self.rowdyid)
			self.assertURLEqual(response.url, "/audit/checklistview/")
			print("Checklist Entry View Called")		


	def test_bUpdate(self):

		client=Client()
		client.login(username='Binoy',password='admin@123')
		#Project Updation Testing
		self.rowdyid=Process_Checklist.objects.latest('id').id

		print("MAjama : ",self.rowdyid)
		req_data = {
			"checklist_title": "Binoy",
			"description": "Checks whether the code is optimized, standard and error free.",
			"weightage": 40,
			"group": "Code Quality"
		}	

		url=reverse('checklistupdate', kwargs={'pk': int(self.rowdyid)})
		#print(url)
		response = client.post(url, req_data)
		if response.status_code==404:
			print("Page not found")
		else:
			print(Process_Checklist.objects.get(id=int(self.rowdyid)).checklist_title)
			print("Process Checklist Update View successfully called")
			self.assertURLEqual(response.url, "/audit/checklistview")


	def test_cDelete(self):
		client=Client()
		client.login(username='Binoy',password='admin@123')
		#Project Updation Testing
		self.rowdyid=Process_Checklist.objects.latest('id').id
		#Project Deletion Testing
		url=reverse('checklistdelete', kwargs={'pk': Process_Checklist.objects.latest('id').id})
		response = client.post(url)
		if response.status_code==404:
			print("Page not found")
		else:
			print("Project Delete View successfully called")
			#print(Project.objects.get(id=7))
			self.assertURLEqual(response.url, "/audit/checklistview")


	'''def setUp(self):
		user=CustomUser.objects.create(username='binoy')
		print(CustomUser.objects.all())
		self.project= Project.objects.create(start_date="8888-12-2",end_date="8888-11-22",team_lead=user)
		self.checklist_item=Process_Checklist.objects.create()
		print(self.checklist_item)
		#print(self.user)'''

	def test_first(self):
		#print("qwe",self.user.first_name,"ads",self.user.phone,self.user.designation,self.user.password)
		pass


# Create your tests here.
