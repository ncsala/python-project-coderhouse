from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from department.forms import DepartmentForm
from department.models import Department



# Create your views here.
def information_department(request):
    return render(request,'department/home_department.html', {})

def list_department(request):
    departamentos = None
    error = None
    mensaje = None
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre_buscado', '')
        
        if nombre == '':
            departamentos = Department.objects.all()
            if not departamentos:
                mensaje = 'Aun no hay departamentos ingresados'
        else:
            try:
                departamentos = Department.objects.filter(name=nombre)
            except:
                error = 'Debe ingresar un departamento valido.'

    return render(request,'department/list_department.html', {'departamentos': departamentos, 'error': error, 'mensaje':mensaje})

def create_department(request):
    
    if request.method == 'POST':
        formulario = DepartmentForm(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            departamento = Department(name=datos['name'], short_name=datos['short_name'])
            try:
                departamento.save()
                return redirect('url-departamentos')
            except:
                error = 'El departamento que quiere ingresar esta repetido.'
                return render(request,'department/create_department.html', {'formulario': formulario, 'error': error})
                
    formulario = DepartmentForm()
    
    return render(request,'department/create_department.html', {'formulario': formulario})
    
    

class DeleteDepartment(LoginRequiredMixin, DeleteView):
    template_name = 'department/delete_department.html'
    model = Department
    login_url = reverse_lazy('url-login-usuario')
    
    success_url = reverse_lazy('url-departamentos')
    
class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'department/update_department.html'
    model = Department
    login_url = reverse_lazy('url-login-usuario')
    
    fields = [
            'name', 
            'short_name', 
            ]
    
    success_url = reverse_lazy('url-departamentos')
