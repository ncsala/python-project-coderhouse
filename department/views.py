from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from department.forms import DepartmentForm
from department.models import Department



# Create your views here.
def information_department(request):
    return render(request,'department/home_department.html', {})

def list_department(request):
    departamentos = None
    error = None
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre_buscado', '')
        
        if nombre == '':
            departamentos = Department.objects.all()
        else:
            try:
                departamentos = Department.objects.filter(name=nombre)
            except:
                error = 'Debe ingresar un departamento valido.'

    return render(request,'department/list_department.html', {'departamentos': departamentos, 'error': error})

def create_department(request):
    if request.method == 'POST':
        formulario = DepartmentForm(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            departamento = Department(name=datos['name'], short_name=datos['short_name'])
            departamento.save()
            return redirect('url-departamentos')
    
    formulario = DepartmentForm()
    
    return render(request,'department/create_department.html', {'formulario': formulario})
    

