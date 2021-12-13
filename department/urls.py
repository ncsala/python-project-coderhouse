from django.urls.conf import path
from .views import create_department, information_department, list_department

urlpatterns = [
    path('', information_department, name='url-information_department'),
    path('lista-departamentos/', list_department, name='url-departamentos'),
    path('crear-departamentos/', create_department, name='url-crear-departamentos'),
]



