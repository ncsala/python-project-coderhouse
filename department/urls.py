from django.urls.conf import path
from .views import list_department

urlpatterns = [
    path('', list_department, name='list_department') 
]