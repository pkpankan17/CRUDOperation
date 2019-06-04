from django import forms
from EmpApp.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta :
        model=Employee
        fields='__all__'
'''class EmployeeForm(forms.Form)
    EiD=forms.ImageField()
    ename=forms.CharField()
    Salary=forms.FloatField()'''
