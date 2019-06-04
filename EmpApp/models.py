from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=50)
    salary=models.FloatField()
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.ename;
