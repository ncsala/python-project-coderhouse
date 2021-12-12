from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def HomeView(request):
    # Vista que carga la pagina de inicio
    return render(request,'inicio/index.html', {})

