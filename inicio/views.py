from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def inicio(request):
    return render(request,'inicio/a.html', {})