from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


def Employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "Employee/employee_list.html", context)


def Employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            Employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=Employee)
        return render(request, "Employee/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            Employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= Employee)
        if form.is_valid():
                 form.save()
        return redirect('/employee/list')


def Employee_delete(request,id):
    Employee = Employee.objects.get(pk=id)
    Employee.delete()
    return redirect('/employee/list')