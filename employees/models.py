from django.db import models

from department.models import Department

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Empleado {self.id} - {self.first_name} - {self.last_name} - {self.position} - {self.department}' 