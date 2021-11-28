from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_employees(request):
    return HttpResponse('<h1>Empleadooos!</h1>')
