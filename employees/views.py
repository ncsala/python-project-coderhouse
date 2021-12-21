from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
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
        # order = self.request.GET.get("order", '')
        
        queryset = Employee.objects.search_employee(palabra_clave)
        return queryset

        
class CreateEmployee(CreateView):
    template_name = 'employees/create_employees.html'
    model = Employee
    fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phoneNumber',
            'mobile_phone',
            'position',
            'department',
            'avatar_employees',
            ]
    
    # Para que redireccione cuando se ha completado correctamente
    success_url = reverse_lazy('url-empleados')
    
    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.full_name = employee.first_name + ' ' + employee.last_name
        employee.save()
        
        return super(CreateEmployee, self).form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'employees/update_employees.html'
    model = Employee
    login_url = reverse_lazy('url-login-usuario')
    
    fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phoneNumber',
            'mobile_phone',
            'position',
            'department',
            'avatar_employees', 
            ]
    
    success_url = reverse_lazy('url-empleados')
    
class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'employees/delete_employees.html'
    model = Employee
    login_url = reverse_lazy('url-login-usuario')
    
    success_url = reverse_lazy('url-empleados')


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/detail_employee.html'

