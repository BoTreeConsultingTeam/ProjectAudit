from django.urls import include, path
from user import views

urlpatterns = [
    path('usercreate/', views.UserCreation.as_view(), name='usercreate'),
    path('userreg/', views.UserReg.as_view(), name='userreg'),
    path('index/', views.UserListView.as_view(), name='index'),
    path('userupdate/(?P<pk>[\w-]+)', views.UserUpdate.as_view(), name='userupdate'),
    path('userdelete/(?P<pk>[\w-]+)', views.UserDelete.as_view(), name='userdelete'),
 ]