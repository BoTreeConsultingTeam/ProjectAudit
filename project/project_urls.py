from django.urls import include, path
from project import views

urlpatterns = [
    path('projectcreate/', views.ProjectReg.as_view(), name='projectcreate'),
    path('projectlist/', views.ProjectListView.as_view(), name='projectlist'),
    path('projectupdate/(?P<pk>[\w-]+)', views.ProjectUpdate.as_view(), name='projectupdate'),
    path('projectdelete/(?P<pk>[\w-]+)', views.ProjectDelete.as_view(), name='projectdelete'),
 ]