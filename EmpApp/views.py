from django.shortcuts import render
from django.http import HttpResponse
from EmpApp.models import Employee
from EmpApp.forms import EmployeeForm
# Create your views here.
def ViewEmp(request):
    emplist=Employee.objects.all()
    mydict={"emplist": emplist}
    return render(request,"EmpApp/Employee.html",context=mydict)
def AddEmp(request):
    empform=EmployeeForm()
    mydict={"myform":empform}
    return render(request,'EmpApp/AddEmp.html',context=mydict)
def employeeForm(request):
    form=EmployeeForm()
    mydict={'myform':form}
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        print('data inserted in DB..')
    return render(request,'EmpApp/addEmp.html',context=mydict)
