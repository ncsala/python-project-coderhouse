
from django.urls import path
from django.urls.conf import include
from .views import inicio



urlpatterns = [
    path('', inicio),
    path('empleados/', include('employees.urls')),
    path('departamentos/', include('department.urls')),
]