from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    dept = models.CharField(Department, max_length=100)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.CharField(max_length=100)
    phone = models.IntegerField()
    hiredate =models.DateField()
    
    def __str__(self):
        return "%s %s  %s" %(self.fname,self.lname, self.phone)
    
    