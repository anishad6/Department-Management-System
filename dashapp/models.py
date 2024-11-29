from django.db import models


# Create your models here.

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True) 
    DepartmentName=models.CharField(max_length=100)
    Description=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    status=models.BooleanField(default=True)
    

