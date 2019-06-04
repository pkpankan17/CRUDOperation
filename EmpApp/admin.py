from django.contrib import admin

# Register your models here.
from EmpApp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid','ename','salary']
admin.site.register(Employee,EmployeeAdmin)
