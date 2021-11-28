from django.urls.conf import path
from .views import information_department

urlpatterns = [
    path('', information_department, name='information_department') 
]