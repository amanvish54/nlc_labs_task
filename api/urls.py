from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name='apiOverview'),
    path('employee-list/', views.ShowEmployeesList, name='employee-list'),
    path('employee-add/',views.addEmployee, name='employee-add'),
    path('employee-detail/<int:pk>/', views.ShowEmployee, name='employee-detail'),
    path('employee-delete/<int:pk>/', views.deleteEmployee, name='employee-delete'),
    path('employee-update/', views.updateEmployee, name='employee-update'),
    
]