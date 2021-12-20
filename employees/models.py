from django.db import models
from django.core.validators import RegexValidator

from department.models import Department
from .manager import EmployeeManager


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    mobile_phone = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar_employees = models.ImageField(upload_to='employees', blank=True, null=True)
    
    objects = EmployeeManager()
    
    
    def __str__(self):
        return f'Empleado {self.id} - {self.first_name} - {self.last_name} - {self.position} - {self.department}' 

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name