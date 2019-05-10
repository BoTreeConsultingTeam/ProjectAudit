from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .user_forms import CustomUserCreationForm,RegisterUserForm,UserUpdateForm
from django import forms
from django.views import View,generic
from .models import CustomUser
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.views.generic.edit import UpdateView,DeleteView
from django.core.mail import send_mail
from django.conf import settings
from .tasks import *
#import requests

# Create your views here.


class UserCreation(View):

	def get(self, request):
		form = CustomUserCreationForm()
		return render(request, 'user/usercreation.html', {'form': form})
	def post(self, request):
		#print(str(request.POST['thumb']))
		if request.method == 'POST':
			form = CustomUserCreationForm(request.POST)
			print(form, "hi")
			if form.is_valid():
				print("hi")
				#print(str(request.POST['thumb']))
				#print(form.save().query())
				form.save()
				if request.POST['designation']=="Tech Lead":
					mails(request.POST['email'])
				return redirect('index')
				#return render(request, 'signup/userlistview.html')
		else:
			form = CustomUserCreationForm()
		return render(request, 'user/usercreation.html', {'form': form})


class UserReg(LoginRequiredMixin,View):
	#@login_required(login_url='/accounts/login')
	def get(self, request):
		form = RegisterUserForm()
		return render(request, 'user/userreg.html', {'form': form})
	def post(self, request):
		#print(str(request.POST['thumb']))
		if request.method == 'POST':
			form = RegisterUserForm(request.POST)
			#print(form, "hi")
			if form.is_valid():
				print("hi")
				#print(str(request.POST['thumb']))
				#print(form.save().query())
				print(request.POST['phone'])
				print(request.POST['password'])
				form.save()
				if request.POST['designation']=="Tech Lead":
					mails(request.POST['email'])
				return redirect('index')
				return HttpResponse("Hi")
				#return render(request, 'signup/userlistview.html')
		else:
		    form = RegisterUserForm()
		return render(request, 'user/userreg.html', {'form': form})

class UserListView(LoginRequiredMixin,generic.ListView):
	login_url = '/accounts/login/'
	template_name = 'user/userlistview.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		print(CustomUser.objects.all())
		return CustomUser.objects.all()

class UserUpdate(LoginRequiredMixin,UpdateView):
	model = CustomUser
	form_class = UserUpdateForm
	#fields = ['first_name','last_name','username','email','phone','technology', 'year_of_exp']
	template_name = 'user/userupdate.html'
	success_url = '/user/index'

class UserDelete(LoginRequiredMixin,DeleteView):
	model = CustomUser
	template_name = 'user/userdelete.html'
	success_url = '/user/index'