from django import forms

class EmpleadosFormulario(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name =  forms.CharField(max_length=50)
    position =  forms.CharField(max_length=50)
    

class ChiefsForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)