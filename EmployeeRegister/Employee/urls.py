from django.urls import path
from . import views

urlpatterns = [
    path('', views.Employee_form,name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.Employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.Employee_delete,name='employee_delete'),
    path('list/',views.Employee_list,name='employee_list') # get req. to retrieve and display all records
]