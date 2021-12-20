from django.db import models
from django.db.models import Q

class EmployeeManager(models.Manager):

    def search_employee(self, kword):
        consulta = self.filter(
            Q(id__icontains=kword) | Q(first_name__icontains=kword) | Q(last_name__icontains=kword)
        )

        return consulta
    
