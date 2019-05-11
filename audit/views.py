from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .audit_forms import Process_Checklist_Entry, AuditForm, ChecklistForm
from django.views import View,generic
from .models import Process_Checklist, Audits, Audit_Items
from project.models import Project
from user.models import CustomUser
from django.contrib.auth.mixins import *
from django.views.generic import UpdateView,DeleteView,TemplateView
from django.shortcuts import render, redirect,render_to_response,get_object_or_404
from datetime import date
from django.db import IntegrityError, transaction
import json
import jsonpickle
from .tasks import *
from .models import *



class ChecklistEntry(View):
	def get(self, request):
		form = Process_Checklist_Entry()
		return render(request, 'audit/checklistentry.html', {'form': form})
	def post(self, request):
		if request.method == 'POST':
		    form = Process_Checklist_Entry(request.POST)
		    if form.is_valid():
		        print("hi")
		        form.save()
		        return redirect('checklistview')
		else:
		    form = Process_Checklist_Entry()
		return render(request, 'audit/checklistentry.html', {'form': form})

class ChecklistView(LoginRequiredMixin,generic.ListView):
	login_url = '/accounts/login/'
	template_name = 'audit/checklistview.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		print(Process_Checklist.objects.all())
		return Process_Checklist.objects.all()

class ChecklistUpdate(LoginRequiredMixin,UpdateView):
	model = Process_Checklist
	form_class = Process_Checklist_Entry
	template_name = 'audit/checklistupdate.html'
	success_url = '/audit/checklistview'

class ChecklistDelete(LoginRequiredMixin,DeleteView):
	model = Process_Checklist
	template_name = 'audit/checklistdelete.html'
	success_url = '/audit/checklistview'


class AuditReportCreate(View):
	def get(self, request):
		form = AuditForm()
		sub_form = ChecklistForm(prefix="check")
		group=Process_Checklist.objects.all().values('group').distinct()
		return render(request, 'audit/auditreport.html', {'form': form, 'checklist': checklist, 'group': group, 'sub_form': sub_form})
	def post(self, request):
		if request.method == 'POST':
			try:
				with transaction.atomic():
					form = AuditForm(request.POST)
					sub_form = ChecklistForm(request.POST, prefix="check")
					#print(sub_form)
					sub_form.audit_id=1
					#sub_form.checklist_id=
					rate=0
					items=Process_Checklist.objects.all()
					if form.is_valid():
						print("hi")
						form.average_rating=rate/len(items)
						print(form,form.average_rating)
						print("hi")
						form.save()
						#return redirect('checklistview')

					audits=Audits.objects.all()
					auditid=audits[len(Audits.objects.all())-1].id
					#auditid=1
					for item in items:
						sub_form.comment=request.POST.get('comment-'+str(item.id))
						sub_form.rating=request.POST.get('rating-'+str(item.id))
						rate+=int(request.POST.get('rating-'+str(item.id)))
						sub_form.date=date.today()
						sub_form.audit_id=auditid
						sub_form.checklist_id=item.id
						#print(sub_form.comment, sub_form.rating, sub_form.date, sub_form.audit_id, sub_form.checklist_id)
						audit_items=Audit_Items.objects.create(comment=sub_form.comment, rating=sub_form.rating, date=date.today(), audit_id=auditid, checklist_id=item.id)
						audit_items.save()
						'''print(sub_form)
						if sub_form.is_valid():
							print("asdasidl")
							print(sub_form)
							sub_form.save()
							#return redirect('checklistview')'''
					Audits.objects.filter(id=auditid).update(average_rating=rate/len(items))
					sender={}
					sender['comment']=request.POST['general_comment']
					sender['rating']=str(Audits.objects.get(id=auditid).average_rating)
					sender['admin_email']=str(CustomUser.objects.get(designation="Admin").email)
					sender['lead_email']=str(Project.objects.get(id=request.POST['project']).team_lead.email)
					sender['admin_username']=str(CustomUser.objects.get(designation="Admin").username)
					sender['lead_username']=str(Project.objects.get(id=request.POST['project']).team_lead.username)
					print(sender['lead_email'])
					sender['title']=request.POST['audit_title']
					sender['date']=request.POST['date']
					mails.delay(sender)
					return redirect('checklistview')
			except IntegrityError:
				print("One of the trasnsaction didn't work properly so all transactions rolled back")


		else:
			form = AuditForm()
		return render(request, 'audit/auditreport.html', {'form': form})


class AuditReportView(LoginRequiredMixin,generic.ListView):
	login_url = '/accounts/login/'
	template_name = 'audit/auditreportview.html'
	context_object_name = 'user_list'
	
	def get_queryset(self):
		print(Audits.objects.all())
		return Audits.objects.all()

class AuditItemsView(View):
	
	model = Audit_Items
	template_name = 'audit/audititemsview.html'
	'''def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		id = kwargs.get('pk')
		print(id)
		context = self.get_context_data(object=self.object)
		print(context)
		return render(request,'audit/audititemsview.html')'''

	def get(self, request):
		id1 = request.GET.get('id')
		x = Audit_Items.objects.filter(audit_id=id1)
		print(x)
		return render(request, 'audit/audititemsview.html', {'x': x})



'''class AuditChart(TemplateView):

	template_name= 'audit/auditchart.html'



	def get_context_data(self, **kwargs):
		#print(self.objects.pk)



		user = Audits.objects.all()
		context={}
		context['python_object'] = jsonpickle.encode(user)
		return render('audit/auditchart.html', context)
		#return user
		print('hi',user)
		#form1=CustomUser.objects.filter(ownnershipstatus='applied')
		#return {'form' : form1}'''

class AuditChart(generic.ListView):
	'''def get(self, request):
		x=list(Audits.objects.all().values_list('date',flat=True))
		y=list(Audits.objects.all().values_list('average_rating',flat=True))
		user = Audits.objects.all()
		context = {}
		context['python_object'] = jsonpickle.encode(user)
		#return render('audit/auditchart.html', context)
		return render(request, 'audit/checklistentry.html', {'x': x, 'y': y})'''
	template_name = 'audit/auditchart.html'
	context_object_name = 'user_list'

	def get_queryset(self):
		print(Audits.objects.all())
		xy=list(Audits.objects.all().values('date','average_rating'))
		x = tuple(Audits.objects.all().values_list('date', flat=True))
		y = tuple(Audits.objects.all().values_list('average_rating', flat=True))
		print(x,y)
		#df=pd.DataFrame({'x': range(1,10), 'y': np.random.randn(9)*80+range(1,10) })
		return xy



'''def CityLookup(request,pk):
    cou=serializers.serialize('json',City.objects.all().filter(region_id=pk))
    cou1=serializers.serialize('json',City.objects.all().filter(region_id=pk))
    j={'cou':cou, 'cou1':cou1}

    return JsonResponse(j,safe=False)'''
	
# Create your views here.
