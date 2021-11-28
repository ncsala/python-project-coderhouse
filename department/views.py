from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def information_department(request):
    return render(request,'department/index.html', {})
