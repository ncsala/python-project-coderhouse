from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_department(request):
    return HttpResponse('<h1>Departamentoooos!</h1>')
