
from django.urls import path
from django.urls.conf import include
from .views import HomeView



urlpatterns = [
    path('', HomeView, name='url-inicio'),
    path('empleados/', include('employees.urls')),
    path('departamentos/', include('department.urls')),
]