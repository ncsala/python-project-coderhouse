from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView, DetailView
from employees.forms import EmpleadosFormulario
from .models import Employee
from django.urls import reverse_lazy


# Create your views here.
def information_employees(request):
    return render(request,'employees/home_employees.html', {})
    
class ListEmployees(ListView):
    template_name = 'employees/list_employees.html'
    context_object_name = 'employees'
    paginate_by = 10
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Employee.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

class ListEmployeesAdmin(ListView):
    template_name = 'employees/admin_employees.html'
    context_object_name = 'employees'
    paginate_by = 10
    model = Employee
        
class CreateEmployee(CreateView):
    template_name = 'employees/create_employees.html'
    model = Employee
    fields = [
            'first_name', 
            'last_name', 
            'position',
            'department' 
            ]
    # Para que redireccione cuando se ha completado correctamente
    success_url = reverse_lazy('url-empleados')

class EmployeeUpdateView(UpdateView):
    template_name = 'employees/update_employees.html'
    model = Employee
    
    fields = [
            'first_name', 
            'last_name', 
            'position',
            'department', 
            ]
    
    success_url = reverse_lazy('url-empleados')

class EmployeeDeleteView(DeleteView):
    template_name = 'employees/delete_employees.html'
    model = Employee
    success_url = reverse_lazy('url-empleados')

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/detail_employee.html'


# def list_employees(request):
#     empleados = None
#     error = None
    
#     if request.method == 'GET':
#         nombre = request.GET.get('nombre_buscado', '')
        
#         if nombre == '':
#             empleados = Employee.objects.all()
#         else:
#             try:
#                 empleados = Employee.objects.filter(first_name=nombre)
#             except:
#                 error = 'Debe ingresar un nombre valido.'

#     return render(request,'employees/list_employees.html', {'empleados': empleados, 'error': error})

# def create_employees(request, id):
#     id_empleado = 0
#     try:
#         empleado = Employee.objects.get(id=id)
#         id_empleado = empleado.id
#     except Exception as e:
#         empleado = None
    
#     if request.method == 'POST':
#         formulario = EmpleadosFormulario(request.POST)
        
#         if formulario.is_valid():
#             datos = formulario.cleaned_data
#             empleado = Employee(first_name=datos['first_name'], last_name=datos['last_name'], position=datos['position'])
#             empleado.save()
#             return redirect('url-empleados')
#     elif empleado:
#         formulario = EmpleadosFormulario({'first_name':empleado.first_name, 'last_name':empleado.last_name, 'position':empleado.position})
#     else:
#         id_empleado = 0
#         formulario = EmpleadosFormulario()
    
#     return render(request,'employees/create_employees.html', {'empleado': empleado, 'formulario': formulario, 'idempleado': id_empleado})

# def list_chiefs(request):
    
    # jefes = None
    # error = None
    
    # if request.method == 'GET':
    #     nombre = request.GET.get('nombre_buscado', '')
        
    #     if nombre == '':
    #         jefes = Chief.objects.all()
    #     else:
    #         try:
    #             jefes = Chief.objects.filter(first_name=nombre)
    #         except:
    #             error = 'Debe ingresar un nombre valido.'

    # return render(request,'employees/list_chiefs.html', {'jefes': jefes, 'error': error})

# def create_chiefs(request):
    # if request.method == 'POST':
    #     formulario = ChiefsForm(request.POST)
        
    #     if formulario.is_valid():
    #         datos = formulario.cleaned_data
    #         jefe = Chief(first_name=datos['first_name'], last_name=datos['last_name'])
    #         jefe.save()
    #         return redirect('url-jefes')
    
    # formulario = ChiefsForm()
    
    # return render(request,'employees/create_chiefs.html', {'formulario': formulario})
