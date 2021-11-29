from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from employees.forms import ChiefsForm, EmpleadosFormulario
from .models import Employee, Chief

# Create your views here.
def information_employees(request):
    return render(request,'employees/home_employees.html', {})

def list_employees(request):
    empleados = None
    error = None
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre_buscado', '')
        
        if nombre == '':
            empleados = Employee.objects.all()
        else:
            try:
                empleados = Employee.objects.filter(first_name=nombre)
            except:
                error = 'Debe ingresar un nombre valido.'

    return render(request,'employees/list_employees.html', {'empleados': empleados, 'error': error})

def create_employees(request):
    if request.method == 'POST':
        formulario = EmpleadosFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            empleado = Employee(first_name=datos['first_name'], last_name=datos['last_name'], position=datos['position'])
            empleado.save()
            return redirect('url-empleados')
    
    formulario = EmpleadosFormulario()
    
    return render(request,'employees/create_employees.html', {'formulario': formulario})
    

def list_chiefs(request):
    
    jefes = None
    error = None
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre_buscado', '')
        
        if nombre == '':
            jefes = Chief.objects.all()
        else:
            try:
                jefes = Chief.objects.filter(first_name=nombre)
            except:
                error = 'Debe ingresar un nombre valido.'

    return render(request,'employees/list_chiefs.html', {'jefes': jefes, 'error': error})

def create_chiefs(request):
    if request.method == 'POST':
        formulario = ChiefsForm(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            jefe = Chief(first_name=datos['first_name'], last_name=datos['last_name'])
            jefe.save()
            return redirect('url-jefes')
    
    formulario = ChiefsForm()
    
    return render(request,'employees/create_chiefs.html', {'formulario': formulario})