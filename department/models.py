from django.db import models

# Create your models here.class Department(models.Model):
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=20, blank=True)
    anulate = models.BooleanField(default=False)
    
