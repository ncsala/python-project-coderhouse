from django.urls.conf import path
from .views import create_chiefs, create_employees, information_employees, list_employees, list_chiefs

urlpatterns = [
    path('', information_employees, name='url-informacion-empleados'),
    path('lista-empleados', list_employees, name='url-empleados'),
    path('crear-empleados', create_employees, name='url-crear-empleados'),
    path('lista-jefes', list_chiefs, name='url-jefes'),
    path('crear-jefes', create_chiefs, name='url-crear-jefes'),
]