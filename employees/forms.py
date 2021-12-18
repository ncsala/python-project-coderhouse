from django import forms
from department.models import Department

class EmpleadosFormulario(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name =  forms.CharField(max_length=50)
    position =  forms.CharField(max_length=50)
    # department = forms.ModelChoiceField(queryset=Department)
    
