from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .project_forms import RegisterUserForm
from django.views import View,generic
from .models import Project
from user.models import CustomUser
from django.contrib.auth.mixins import *
from django.views.generic.edit import UpdateView,DeleteView
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from .tasks import *

class ProjectReg(View):
	#@login_required(login_url='/accounts/login')
	def get(self, request):
		form = RegisterUserForm()
		return render(request, 'project/projectcreate.html', {'form': form})
	def post(self, request):
		#print(str(request.POST['thumb']))
		if request.method == 'POST':
			form = RegisterUserForm(request.POST)
			#print(form, "hi")
			if form.is_valid():
				#print("hi")
				#print(str(request.POST['thumb']))
				#print(form.save().query())
				form.save()
				sender={}
				sender['title']=request.POST['title']
				sender['email']=str(CustomUser.objects.get(id=request.POST['team_lead']).email)
				sender['username'] = str(CustomUser.objects.get(id=request.POST['team_lead']).username)
				sender['abstract']=str(request.POST['abstract'])
				#print('email',sender)
				mails.delay(sender)
				return redirect('projectlist')
				#return render(request, 'signup/userlistview.html')
		else:
			form = RegisterUserForm()
		return render(request, 'project/projectcreate.html', {'form': form})

class ProjectListView(LoginRequiredMixin,generic.ListView):
	login_url = '/accounts/login/'
	template_name = 'project/projectlistview.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		#print(Project.objects.all())
		return Project.objects.all()

class ProjectUpdate(LoginRequiredMixin,UpdateView):
	model = Project
	form_class = RegisterUserForm
	#fields = ['first_name','last_name','username','email','phone','technology', 'year_of_exp']
	template_name = 'project/projectupdate.html'
	success_url = '/project/projectlist'

class ProjectDelete(LoginRequiredMixin,DeleteView):
	model = Project
	template_name = 'project/projectdelete.html'
	success_url = '/project/projectlist'

# Create your views here.
