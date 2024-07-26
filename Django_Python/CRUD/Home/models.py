from django.db import models

class EmpTbl(models.Model):
    Empid=models.AutoField(max_length=10,primary_key=True)
    EmpName =models.CharField(max_length=50)
    EmpEmail = models.CharField(max_length=50)
    EmpMobile = models.CharField(max_length=50)
    EmpCity = models.CharField(max_length=50)



