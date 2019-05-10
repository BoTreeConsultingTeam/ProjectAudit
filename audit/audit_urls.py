from django.urls import include, path
from audit import views

urlpatterns = [
    path('checklistentry/', views.ChecklistEntry.as_view(), name='checklistentry'),
    path('checklistview/', views.ChecklistView.as_view(), name='checklistview'),
    path('checklistupdate/(?P<pk>[\w-]+)', views.ChecklistUpdate.as_view(), name='checklistupdate'),
    path('checklistdelete/(?P<pk>[\w-]+)', views.ChecklistDelete.as_view(), name='checklistdelete'),
    path('auditreport/', views.AuditReportCreate.as_view(), name='auditreport'),
    path('auditreportview/', views.AuditReportView.as_view(), name='auditreportview'),
    path('audititemsview/', views.AuditItemsView.as_view(), name='audititemsview'),
    path('auditchart', views.AuditChart.as_view(), name='auditchart'),
 ]