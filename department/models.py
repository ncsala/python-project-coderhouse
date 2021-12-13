from django.db import models

# Create your models here.class Department(models.Model):
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f'Departamento {self.id} - {self.name} - {self.short_name}'