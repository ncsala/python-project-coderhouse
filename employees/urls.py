from django.urls.conf import path
from .views import *


urlpatterns = [
    path('', information_employees, name='url-informacion-empleados'),
    path('lista-empleados/', ListEmployees.as_view(), name='url-empleados'),
    # path('lista-empleados-admin/', ListEmployeesAdmin.as_view(), name='url-empleados-admin'),
    path('crear-empleados/', CreateEmployee.as_view(), name='url-crear-empleados'),
    path('actualizar-empleado/<pk>/', EmployeeUpdateView.as_view(), name='url-update'),
    path('eliminar-empleado/<pk>/', EmployeeDeleteView.as_view(), name='url-delete'),
    path('detalle-empleado/<pk>/', EmployeeDetailView.as_view(), name='url-detail'),
]
