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
    path('auditchart/(?P<pk>[0-9]+)/', views.AuditChart.as_view(), name='auditchart'),
    path('auditupdate/(?P<pk>[\w-]+)', views.AuditUpdate.as_view(), name='auditupdate'),
    path('auditdelete/(?P<pk>[\w-]+)', views.AuditDelete.as_view(), name='auditdelete'),
    path('api/chart/data/(?P<pk>[0-9]+)/', views.ListGraph.as_view(), name='chart'),
    path('api/chart/pie/', views.PieGraph.as_view(), name='pie'),
    path('api/data/', views.get_data, name='api-data'),
    path('auditstore/(?P<pk>[0-9]+)/', views.AuditExcelSave.as_view(), name='auditstore'),
 ]