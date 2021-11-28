from django.urls.conf import path
from .views import list_employees

urlpatterns = [
    path('', list_employees, name='list_employees')
        
]